"""
Generate sample images for the Image-to-Hydro simulation notebook
"""

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import os

def create_spiral_galaxy(size=(100, 100), arms=2, tightness=3.0):
    """Create a spiral galaxy pattern"""
    width, height = size
    x = np.linspace(-2, 2, width)
    y = np.linspace(-2, 2, height)
    X, Y = np.meshgrid(x, y)
    
    r = np.sqrt(X**2 + Y**2)
    theta = np.arctan2(Y, X)
    
    # Create spiral arms
    spiral = np.zeros((height, width))
    for arm in range(arms):
        arm_offset = arm * 2 * np.pi / arms
        spiral += np.exp(-r/0.8) * np.maximum(0, np.cos(arms*theta - tightness*r + arm_offset))**3
    
    # Central bulge
    bulge = np.exp(-r**2/0.3**2)
    
    # Combine
    intensity = spiral + 0.3*bulge
    intensity = np.clip(intensity, 0, 1)
    
    # Convert to RGB with galaxy colors
    img_array = np.zeros((height, width, 3))
    img_array[:,:,0] = intensity * 0.8  # Red (old stars)
    img_array[:,:,1] = intensity * 0.9  # Green
    img_array[:,:,2] = intensity + 0.2*spiral  # Blue (young stars in arms)
    
    return np.clip(255 * img_array, 0, 255).astype(np.uint8)

def create_galaxy_collision(size=(120, 80)):
    """Create two interacting galaxies"""
    width, height = size
    x = np.linspace(-3, 3, width)
    y = np.linspace(-2, 2, height)
    X, Y = np.meshgrid(x, y)
    
    # Galaxy 1 (left)
    r1 = np.sqrt((X + 1)**2 + Y**2)
    galaxy1 = np.exp(-r1**2/0.4**2)
    
    # Galaxy 2 (right, slightly tilted)
    r2 = np.sqrt((X - 1)**2 + (Y*1.3)**2)
    galaxy2 = np.exp(-r2**2/0.3**2)
    
    # Interaction/tidal tails (simplified)
    bridge = np.exp(-((X)**2 + (Y*0.3)**2)/0.8**2) * 0.3
    
    intensity = galaxy1 + galaxy2 + bridge
    intensity = np.clip(intensity, 0, 1)
    
    # Convert to RGB
    img_array = np.stack([intensity*0.9, intensity*0.7, intensity*1.0], axis=2)
    return np.clip(255 * img_array, 0, 255).astype(np.uint8)

def create_simple_face(size=(80, 80)):
    """Create a simple smiley face"""
    width, height = size
    x = np.linspace(-1.5, 1.5, width)
    y = np.linspace(-1.5, 1.5, height)
    X, Y = np.meshgrid(x, y)
    
    r = np.sqrt(X**2 + Y**2)
    
    # Face outline
    face = ((r < 1.2) & (r > 1.0)).astype(float)
    
    # Eyes
    left_eye = ((X + 0.4)**2 + (Y + 0.3)**2) < 0.15**2
    right_eye = ((X - 0.4)**2 + (Y + 0.3)**2) < 0.15**2
    
    # Mouth (smile)
    mouth_r = np.sqrt(X**2 + (Y + 0.2)**2)
    mouth = ((mouth_r < 0.6) & (mouth_r > 0.4) & (Y < -0.2)).astype(float)
    
    # Combine
    intensity = face + left_eye + right_eye + mouth
    intensity = np.clip(intensity, 0, 1)
    
    # Yellow smiley
    img_array = np.stack([intensity, intensity, intensity*0.3], axis=2)
    return np.clip(255 * img_array, 0, 255).astype(np.uint8)

def create_logo_pattern(size=(90, 90)):
    """Create a simple logo-like pattern"""
    width, height = size
    x = np.linspace(-1, 1, width)
    y = np.linspace(-1, 1, height)
    X, Y = np.meshgrid(x, y)
    
    # Create a stylized 'S' pattern
    # Central curve
    t = np.linspace(-2*np.pi, 2*np.pi, 200)
    s_x = 0.5 * np.sin(t)
    s_y = 0.8 * np.sin(2*t) * np.sin(t)
    
    # Create image by finding distances to the curve
    intensity = np.zeros((height, width))
    
    for i, (sx, sy) in enumerate(zip(s_x, s_y)):
        # Distance from each point to curve
        dist = np.sqrt((X - sx)**2 + (Y - sy)**2)
        intensity += np.exp(-dist**2/0.1**2)
    
    # Add some structure
    r = np.sqrt(X**2 + Y**2)
    border = ((r < 0.9) & (r > 0.8)).astype(float) * 0.5
    intensity += border
    
    intensity = np.clip(intensity, 0, 1)
    
    # Convert to RGB (blue-ish)
    img_array = np.stack([intensity*0.3, intensity*0.6, intensity], axis=2)
    return np.clip(255 * img_array, 0, 255).astype(np.uint8)

def save_sample_images():
    """Generate and save all sample images"""
    
    # Create output directory
    os.makedirs('../sample_images', exist_ok=True)
    
    # Generate images
    spiral = create_spiral_galaxy()
    collision = create_galaxy_collision()
    face = create_simple_face()
    logo = create_logo_pattern()
    
    # Save as PNG files
    Image.fromarray(spiral).save('../sample_images/spiral_galaxy.png')
    Image.fromarray(collision).save('../sample_images/galaxy_collision.png')
    Image.fromarray(face).save('../sample_images/smiley_face.png')
    Image.fromarray(logo).save('../sample_images/logo_pattern.png')
    
    print("Sample images created:")
    print("  • spiral_galaxy.png - Classic spiral galaxy")
    print("  • galaxy_collision.png - Two interacting galaxies")
    print("  • smiley_face.png - Simple smiley face")
    print("  • logo_pattern.png - Stylized pattern")
    
    # Create a preview plot
    fig, axes = plt.subplots(2, 2, figsize=(12, 12))
    
    axes[0,0].imshow(spiral)
    axes[0,0].set_title('Spiral Galaxy')
    axes[0,0].axis('off')
    
    axes[0,1].imshow(collision)
    axes[0,1].set_title('Galaxy Collision')
    axes[0,1].axis('off')
    
    axes[1,0].imshow(face)
    axes[1,0].set_title('Smiley Face')
    axes[1,0].axis('off')
    
    axes[1,1].imshow(logo)
    axes[1,1].set_title('Logo Pattern')
    axes[1,1].axis('off')
    
    plt.suptitle('Sample Images for Image-to-Hydro Simulations', fontsize=16)
    plt.tight_layout()
    plt.savefig('../sample_images/sample_preview.png', dpi=150, bbox_inches='tight')
    plt.close()
    
    print("  • sample_preview.png - Preview of all samples")

if __name__ == "__main__":
    save_sample_images()