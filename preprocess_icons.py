import os
import glob
import logging
import io
from PIL import Image
import numpy as np
import cairosvg
from tqdm import tqdm

#Configuration
# Input directory containing the original SVG Heroicons
SVG_DIR = '/Users/shrutisaagar/work/op/heroicons/optimized/24' # Adjust path as needed

# Output directory to save processed PNG images
OUTPUT_DIR = '/Users/shrutisaagar/msai/3/genai/icon_gen/processed_icons'

# Desired output image size (width, height)
IMG_SIZE = (64, 64)

# Output mode: 'grayscale' or 'binary'
OUTPUT_MODE = 'binary'

BINARY_THRESHOLD = 128 

#Logging Setup
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

#Main Processing Function
def process_icons(svg_dir, output_dir, img_size, mode='grayscale', threshold=128):
    """
    Finds SVG files, rasterizes, preprocesses, and saves them as PNGs.
    """
    logging.info(f"Starting icon processing...")
    logging.info(f"Source SVG directory: {svg_dir}")
    logging.info(f"Output directory: {output_dir}")
    logging.info(f"Target image size: {img_size}")
    logging.info(f"Output mode: {mode}")
    if mode == 'binary':
        logging.info(f"Binary threshold: {threshold}")

    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    logging.info(f"Ensured output directory exists: {output_dir}")

    # Find all SVG files recursively in the source directory
    svg_files = glob.glob(os.path.join(svg_dir, '**/*.svg'), recursive=True)
    if not svg_files:
        logging.error(f"No SVG files found in {svg_dir}. Please check the path.")
        return

    logging.info(f"Found {len(svg_files)} SVG files to process.")

    processed_count = 0
    error_count = 0

    # Process each SVG file with a progress bar
    for svg_path in tqdm(svg_files, desc="Processing Icons"):
        try:
            # Construct output PNG path, maintaining relative structure if needed
            relative_path = os.path.relpath(svg_path, svg_dir)
            base_name = os.path.splitext(relative_path)[0]
            # Replace path separators for cross-platform compatibility in filename
            safe_base_name = base_name.replace(os.path.sep, '_')
            output_path = os.path.join(output_dir, f"{safe_base_name}.png")

            # 1. Rasterize SVG to PNG bytes in memory at the target size
            png_bytes = cairosvg.svg2png(
                url=svg_path,
                output_width=img_size[0],
                output_height=img_size[1],
                background_color='white'
            )

            # 2. Load PNG bytes into Pillow Image object
            img = Image.open(io.BytesIO(png_bytes))

            # 3. Convert to Grayscale ('L' mode: 0=black, 255=white)
            img_gray = img.convert('L')

            # 4. Binarize
            if mode == 'binary':
                img_array = np.array(img_gray)
                binary_array = ((img_array >= threshold) * 255).astype(np.uint8)
                final_img = Image.fromarray(binary_array, mode='L')

            # 5. Save the processed image as PNG
            final_img.save(output_path)
            processed_count += 1

        except Exception as e:
            logging.error(f"Failed to process {svg_path}: {e}")
            error_count += 1

    logging.info(f"--- Processing Complete ---")
    logging.info(f"Successfully processed: {processed_count} icons")
    logging.info(f"Failed to process: {error_count} icons")
    logging.info(f"Processed icons saved in: {output_dir}")

#Run the script
if __name__ == "__main__":

    process_icons(
        svg_dir=SVG_DIR,
        output_dir=OUTPUT_DIR,
        img_size=IMG_SIZE,
        mode=OUTPUT_MODE,
        threshold=BINARY_THRESHOLD
    )
