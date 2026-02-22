from PIL import Image, ImageDraw, ImageFont
import os

# Create placeholder images for projects
def create_project_placeholder(filename, title, color):
    """Create a placeholder image for a project"""
    # Create image with gradient-like background
    img = Image.new('RGB', (600, 400), color=color)
    draw = ImageDraw.Draw(img)
    
    # Add semi-transparent overlay for text
    overlay = Image.new('RGBA', img.size, (0, 0, 0, 100))
    img.putalpha(255)
    img = img.convert('RGBA')
    img.paste(overlay, (0, 0), overlay)
    img = img.convert('RGB')
    
    # Add text
    try:
        # Try to use a system font
        font = ImageFont.truetype("arial.ttf", 48)
        font_small = ImageFont.truetype("arial.ttf", 24)
    except:
        # Fall back to default font
        font = ImageFont.load_default()
        font_small = ImageFont.load_default()
    
    # Draw title
    draw.text((300, 180), title, fill=(255, 255, 255), font=font, anchor="mm")
    draw.text((300, 240), "Project Screenshot", fill=(200, 200, 200), font=font_small, anchor="mm")
    
    # Create output directory if it doesn't exist
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    
    # Save image
    img.save(filename, 'JPEG', quality=95)
    print(f"Created: {filename}")

# Create placeholders
create_project_placeholder("images/project1.jpg", "ClickVote", (108, 99, 255))  # Purple
create_project_placeholder("images/project2.jpg", "Task Manager", (100, 150, 200))  # Blue
create_project_placeholder("images/project3.jpg", "Weather App", (200, 150, 100))  # Orange
