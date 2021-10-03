from pathlib import Path
import json
import csv
import time

def detect_properties(path):
    """Detects image properties in the file."""
    from google.cloud import vision
    import io
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = []
    response = client.image_properties(image=image)

    path = Path(path)
    print(f'Processing image {path.name}')

    row = []    
    row.append(path.name)
    for color in response.image_properties_annotation.dominant_colors.colors:        
        row.append(color.color.red)
        row.append(color.color.green)
        row.append(color.color.blue)
        row.append(color.score)
        row.append(color.pixel_fraction)
    
    return row

def main():
    count = 0
    pathlist = Path('./images').glob('**/*.png')
    #pathlist = Path('./images').glob('**/000000014*.png')    

    with open('results.csv', mode='w') as results_file:
        results_writer = csv.writer(results_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        cols = ['file']
        extra_cols = [[f'r{i}', f'g{i}', f'b{i}', f'score{i}', f'pixelfraction{i}'] for i in range(1,11)]
        for c in extra_cols:
            cols.extend(c)
        results_writer.writerow(cols)

        for path in pathlist:
            print(f'processing image {count+1}')
            path_in_str = str(path)            
            row = detect_properties(path_in_str)
            results_writer.writerow(row)
            time.sleep(1)
            count += 1            

    print(f'Total Images: {count}')   

if __name__ == "__main__":
    main()