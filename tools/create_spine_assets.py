"""
Creates Aelora body part sprites and Spine skeleton JSON for the game.
Generates colored body part PNGs and a complete Spine JSON with animations.
"""

from PIL import Image, ImageDraw, ImageFilter
import json
import os
import math

OUTPUT_DIR = os.path.expanduser("~/Desktop/premium-mobile-game/Aelora/Assets/Art/Characters/parts")
SPINE_DIR = os.path.expanduser("~/Desktop/premium-mobile-game/Aelora/Assets/Animations")

os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(SPINE_DIR, exist_ok=True)

# Color palette - fairy tale blue dress theme
SKIN_COLOR = (235, 200, 175, 255)
DRESS_COLOR = (50, 90, 180, 255)
DRESS_LIGHT = (80, 120, 210, 255)
HAIR_COLOR = (80, 50, 30, 255)
HAIR_HIGHLIGHT = (120, 80, 50, 255)

def create_body_part(name, width, height, color, shape="rect", details=None):
    """Create a body part sprite with anti-aliased edges."""
    img = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    if shape == "circle":
        draw.ellipse([2, 2, width-3, height-3], fill=color)
    elif shape == "oval":
        draw.ellipse([2, 2, width-3, height-3], fill=color)
    elif shape == "dress":
        # Trapezoid dress shape
        top_width = width * 0.4
        top_offset = (width - top_width) / 2
        points = [
            (top_offset, 0),
            (top_offset + top_width, 0),
            (width - 5, height - 5),
            (5, height - 5)
        ]
        draw.polygon(points, fill=color)
        # Add lighter overlay for depth
        if details:
            overlay_points = [
                (top_offset + top_width * 0.2, 0),
                (top_offset + top_width * 0.6, 0),
                (width * 0.6, height - 5),
                (width * 0.3, height - 5)
            ]
            draw.polygon(overlay_points, fill=details)
    elif shape == "hair":
        # Flowing hair shape
        draw.ellipse([2, 2, width-3, height * 0.5], fill=color)
        # Hair strands flowing down
        for i in range(3):
            x_offset = width * 0.2 + i * width * 0.25
            strand_width = width * 0.15
            draw.ellipse([x_offset, height*0.3, x_offset+strand_width, height-3], fill=color)
        if details:
            draw.ellipse([width*0.3, height*0.1, width*0.7, height*0.4], fill=details)
    else:
        # Rounded rectangle
        radius = min(width, height) // 4
        draw.rounded_rectangle([2, 2, width-3, height-3], radius=radius, fill=color)

    return img

# Create all body parts
parts = {
    "head": (80, 90, SKIN_COLOR, "circle"),
    "hair": (100, 120, HAIR_COLOR, "hair"),
    "torso": (60, 80, DRESS_COLOR, "rect"),
    "upper_arm_l": (25, 55, SKIN_COLOR, "oval"),
    "upper_arm_r": (25, 55, SKIN_COLOR, "oval"),
    "lower_arm_l": (20, 50, SKIN_COLOR, "oval"),
    "lower_arm_r": (20, 50, SKIN_COLOR, "oval"),
    "hand_l": (22, 22, SKIN_COLOR, "circle"),
    "hand_r": (22, 22, SKIN_COLOR, "circle"),
    "dress_upper": (70, 60, DRESS_COLOR, "rect"),
    "dress_lower": (120, 100, DRESS_COLOR, "dress"),
    "upper_leg_l": (28, 60, DRESS_LIGHT, "oval"),
    "upper_leg_r": (28, 60, DRESS_LIGHT, "oval"),
    "lower_leg_l": (22, 55, SKIN_COLOR, "oval"),
    "lower_leg_r": (22, 55, SKIN_COLOR, "oval"),
    "foot_l": (30, 18, DRESS_LIGHT, "oval"),
    "foot_r": (30, 18, DRESS_LIGHT, "oval"),
    "sparkle": (20, 20, (255, 255, 200, 200), "circle"),
}

print("Creating body part sprites...")
for name, (w, h, color, shape) in parts.items():
    details = None
    if name == "dress_lower":
        details = DRESS_LIGHT
    elif name == "hair":
        details = HAIR_HIGHLIGHT
    img = create_body_part(name, w, h, color, shape, details)
    img.save(os.path.join(OUTPUT_DIR, f"{name}.png"))
    print(f"  Created {name}.png ({w}x{h})")

# Now create the Spine JSON skeleton
print("\nCreating Spine skeleton JSON...")

spine_data = {
    "skeleton": {
        "hash": "aelora_v1",
        "spine": "4.2",
        "x": -60,
        "y": 0,
        "width": 120,
        "height": 300,
        "images": "./parts",
        "audio": ""
    },
    "bones": [
        {"name": "root"},
        {"name": "hip", "parent": "root", "y": 120},
        {"name": "spine1", "parent": "hip", "y": 40},
        {"name": "spine2", "parent": "spine1", "y": 40},
        {"name": "neck", "parent": "spine2", "y": 35},
        {"name": "head", "parent": "neck", "y": 30},
        {"name": "hair", "parent": "head", "y": 20},
        # Left arm
        {"name": "shoulder_l", "parent": "spine2", "x": -30, "y": 25},
        {"name": "upper_arm_l", "parent": "shoulder_l", "length": 55, "rotation": -10},
        {"name": "lower_arm_l", "parent": "upper_arm_l", "length": 50, "y": -55},
        {"name": "hand_l", "parent": "lower_arm_l", "y": -50},
        # Right arm
        {"name": "shoulder_r", "parent": "spine2", "x": 30, "y": 25},
        {"name": "upper_arm_r", "parent": "shoulder_r", "length": 55, "rotation": 10},
        {"name": "lower_arm_r", "parent": "upper_arm_r", "length": 50, "y": -55},
        {"name": "hand_r", "parent": "lower_arm_r", "y": -50},
        # Left leg
        {"name": "upper_leg_l", "parent": "hip", "x": -15, "length": 60, "rotation": 0},
        {"name": "lower_leg_l", "parent": "upper_leg_l", "length": 55, "y": -60},
        {"name": "foot_l", "parent": "lower_leg_l", "y": -55},
        # Right leg
        {"name": "upper_leg_r", "parent": "hip", "x": 15, "length": 60, "rotation": 0},
        {"name": "lower_leg_r", "parent": "upper_leg_r", "length": 55, "y": -60},
        {"name": "foot_r", "parent": "lower_leg_r", "y": -55},
        # Dress
        {"name": "dress_top", "parent": "spine1", "y": 0},
        {"name": "dress_bottom", "parent": "hip", "y": -20},
    ],
    "slots": [
        {"name": "dress_lower", "bone": "dress_bottom", "attachment": "dress_lower"},
        {"name": "upper_leg_l", "bone": "upper_leg_l", "attachment": "upper_leg_l"},
        {"name": "lower_leg_l", "bone": "lower_leg_l", "attachment": "lower_leg_l"},
        {"name": "foot_l", "bone": "foot_l", "attachment": "foot_l"},
        {"name": "upper_leg_r", "bone": "upper_leg_r", "attachment": "upper_leg_r"},
        {"name": "lower_leg_r", "bone": "lower_leg_r", "attachment": "lower_leg_r"},
        {"name": "foot_r", "bone": "foot_r", "attachment": "foot_r"},
        {"name": "dress_upper", "bone": "dress_top", "attachment": "dress_upper"},
        {"name": "torso", "bone": "spine2", "attachment": "torso"},
        {"name": "upper_arm_l", "bone": "upper_arm_l", "attachment": "upper_arm_l"},
        {"name": "lower_arm_l", "bone": "lower_arm_l", "attachment": "lower_arm_l"},
        {"name": "hand_l", "bone": "hand_l", "attachment": "hand_l"},
        {"name": "upper_arm_r", "bone": "upper_arm_r", "attachment": "upper_arm_r"},
        {"name": "lower_arm_r", "bone": "lower_arm_r", "attachment": "lower_arm_r"},
        {"name": "hand_r", "bone": "hand_r", "attachment": "hand_r"},
        {"name": "head", "bone": "head", "attachment": "head"},
        {"name": "hair", "bone": "hair", "attachment": "hair"},
    ],
    "skins": [
        {
            "name": "default",
            "attachments": {
                "head": {"head": {"width": 80, "height": 90}},
                "hair": {"hair": {"width": 100, "height": 120, "y": 20}},
                "torso": {"torso": {"width": 60, "height": 80}},
                "dress_upper": {"dress_upper": {"width": 70, "height": 60}},
                "dress_lower": {"dress_lower": {"width": 120, "height": 100}},
                "upper_arm_l": {"upper_arm_l": {"width": 25, "height": 55}},
                "lower_arm_l": {"lower_arm_l": {"width": 20, "height": 50}},
                "hand_l": {"hand_l": {"width": 22, "height": 22}},
                "upper_arm_r": {"upper_arm_r": {"width": 25, "height": 55}},
                "lower_arm_r": {"lower_arm_r": {"width": 20, "height": 50}},
                "hand_r": {"hand_r": {"width": 22, "height": 22}},
                "upper_leg_l": {"upper_leg_l": {"width": 28, "height": 60}},
                "lower_leg_l": {"lower_leg_l": {"width": 22, "height": 55}},
                "foot_l": {"foot_l": {"width": 30, "height": 18}},
                "upper_leg_r": {"upper_leg_r": {"width": 28, "height": 60}},
                "lower_leg_r": {"lower_leg_r": {"width": 22, "height": 55}},
                "foot_r": {"foot_r": {"width": 30, "height": 18}},
            }
        }
    ],
    "animations": {
        "idle": {
            "bones": {
                "spine1": {
                    "rotate": [
                        {"time": 0, "angle": 0},
                        {"time": 0.8, "angle": 2},
                        {"time": 1.6, "angle": 0}
                    ]
                },
                "spine2": {
                    "rotate": [
                        {"time": 0, "angle": 0},
                        {"time": 0.8, "angle": 1},
                        {"time": 1.6, "angle": 0}
                    ]
                },
                "head": {
                    "rotate": [
                        {"time": 0, "angle": 0},
                        {"time": 1.0, "angle": -3},
                        {"time": 1.6, "angle": 0}
                    ]
                },
                "hair": {
                    "rotate": [
                        {"time": 0, "angle": 0},
                        {"time": 0.6, "angle": 5},
                        {"time": 1.2, "angle": -3},
                        {"time": 1.6, "angle": 0}
                    ]
                },
                "upper_arm_l": {
                    "rotate": [
                        {"time": 0, "angle": 0},
                        {"time": 0.8, "angle": 5},
                        {"time": 1.6, "angle": 0}
                    ]
                },
                "upper_arm_r": {
                    "rotate": [
                        {"time": 0, "angle": 0},
                        {"time": 0.8, "angle": -5},
                        {"time": 1.6, "angle": 0}
                    ]
                },
                "dress_bottom": {
                    "rotate": [
                        {"time": 0, "angle": 0},
                        {"time": 0.8, "angle": 3},
                        {"time": 1.6, "angle": 0}
                    ]
                }
            }
        },
        "run": {
            "bones": {
                "hip": {
                    "translate": [
                        {"time": 0, "x": 0, "y": 0},
                        {"time": 0.15, "x": 0, "y": 8},
                        {"time": 0.3, "x": 0, "y": 0},
                        {"time": 0.45, "x": 0, "y": 8},
                        {"time": 0.6, "x": 0, "y": 0}
                    ]
                },
                "spine1": {
                    "rotate": [
                        {"time": 0, "angle": -5},
                        {"time": 0.15, "angle": 5},
                        {"time": 0.3, "angle": -5},
                        {"time": 0.45, "angle": 5},
                        {"time": 0.6, "angle": -5}
                    ]
                },
                "upper_leg_l": {
                    "rotate": [
                        {"time": 0, "angle": -30},
                        {"time": 0.15, "angle": 30},
                        {"time": 0.3, "angle": -30},
                        {"time": 0.45, "angle": 30},
                        {"time": 0.6, "angle": -30}
                    ]
                },
                "lower_leg_l": {
                    "rotate": [
                        {"time": 0, "angle": 40},
                        {"time": 0.15, "angle": -10},
                        {"time": 0.3, "angle": 40},
                        {"time": 0.45, "angle": -10},
                        {"time": 0.6, "angle": 40}
                    ]
                },
                "upper_leg_r": {
                    "rotate": [
                        {"time": 0, "angle": 30},
                        {"time": 0.15, "angle": -30},
                        {"time": 0.3, "angle": 30},
                        {"time": 0.45, "angle": -30},
                        {"time": 0.6, "angle": 30}
                    ]
                },
                "lower_leg_r": {
                    "rotate": [
                        {"time": 0, "angle": -10},
                        {"time": 0.15, "angle": 40},
                        {"time": 0.3, "angle": -10},
                        {"time": 0.45, "angle": 40},
                        {"time": 0.6, "angle": -10}
                    ]
                },
                "upper_arm_l": {
                    "rotate": [
                        {"time": 0, "angle": 25},
                        {"time": 0.15, "angle": -25},
                        {"time": 0.3, "angle": 25},
                        {"time": 0.45, "angle": -25},
                        {"time": 0.6, "angle": 25}
                    ]
                },
                "upper_arm_r": {
                    "rotate": [
                        {"time": 0, "angle": -25},
                        {"time": 0.15, "angle": 25},
                        {"time": 0.3, "angle": -25},
                        {"time": 0.45, "angle": 25},
                        {"time": 0.6, "angle": -25}
                    ]
                },
                "hair": {
                    "rotate": [
                        {"time": 0, "angle": 10},
                        {"time": 0.15, "angle": -10},
                        {"time": 0.3, "angle": 10},
                        {"time": 0.45, "angle": -10},
                        {"time": 0.6, "angle": 10}
                    ]
                },
                "dress_bottom": {
                    "rotate": [
                        {"time": 0, "angle": 8},
                        {"time": 0.15, "angle": -8},
                        {"time": 0.3, "angle": 8},
                        {"time": 0.45, "angle": -8},
                        {"time": 0.6, "angle": 8}
                    ]
                }
            }
        },
        "jump": {
            "bones": {
                "hip": {
                    "translate": [
                        {"time": 0, "x": 0, "y": 0},
                        {"time": 0.1, "x": 0, "y": -10},
                        {"time": 0.3, "x": 0, "y": 30},
                        {"time": 0.6, "x": 0, "y": 20},
                        {"time": 0.8, "x": 0, "y": 0}
                    ]
                },
                "upper_leg_l": {
                    "rotate": [
                        {"time": 0, "angle": 0},
                        {"time": 0.1, "angle": 30},
                        {"time": 0.3, "angle": -20},
                        {"time": 0.6, "angle": -15},
                        {"time": 0.8, "angle": 0}
                    ]
                },
                "upper_leg_r": {
                    "rotate": [
                        {"time": 0, "angle": 0},
                        {"time": 0.1, "angle": 30},
                        {"time": 0.3, "angle": 15},
                        {"time": 0.6, "angle": 10},
                        {"time": 0.8, "angle": 0}
                    ]
                },
                "upper_arm_l": {
                    "rotate": [
                        {"time": 0, "angle": 0},
                        {"time": 0.2, "angle": -40},
                        {"time": 0.5, "angle": -30},
                        {"time": 0.8, "angle": 0}
                    ]
                },
                "upper_arm_r": {
                    "rotate": [
                        {"time": 0, "angle": 0},
                        {"time": 0.2, "angle": 40},
                        {"time": 0.5, "angle": 30},
                        {"time": 0.8, "angle": 0}
                    ]
                },
                "hair": {
                    "rotate": [
                        {"time": 0, "angle": 0},
                        {"time": 0.2, "angle": 20},
                        {"time": 0.6, "angle": -15},
                        {"time": 0.8, "angle": 0}
                    ]
                },
                "dress_bottom": {
                    "rotate": [
                        {"time": 0, "angle": 0},
                        {"time": 0.2, "angle": 15},
                        {"time": 0.6, "angle": -10},
                        {"time": 0.8, "angle": 0}
                    ]
                }
            }
        },
        "slide": {
            "bones": {
                "hip": {
                    "translate": [
                        {"time": 0, "x": 0, "y": 0},
                        {"time": 0.1, "x": 0, "y": -60},
                        {"time": 0.5, "x": 0, "y": -60},
                        {"time": 0.6, "x": 0, "y": 0}
                    ],
                    "rotate": [
                        {"time": 0, "angle": 0},
                        {"time": 0.1, "angle": -70},
                        {"time": 0.5, "angle": -70},
                        {"time": 0.6, "angle": 0}
                    ]
                },
                "spine1": {
                    "rotate": [
                        {"time": 0, "angle": 0},
                        {"time": 0.1, "angle": -20},
                        {"time": 0.5, "angle": -20},
                        {"time": 0.6, "angle": 0}
                    ]
                },
                "upper_leg_l": {
                    "rotate": [
                        {"time": 0, "angle": 0},
                        {"time": 0.1, "angle": 60},
                        {"time": 0.5, "angle": 60},
                        {"time": 0.6, "angle": 0}
                    ]
                },
                "lower_leg_l": {
                    "rotate": [
                        {"time": 0, "angle": 0},
                        {"time": 0.1, "angle": -30},
                        {"time": 0.5, "angle": -30},
                        {"time": 0.6, "angle": 0}
                    ]
                },
                "upper_leg_r": {
                    "rotate": [
                        {"time": 0, "angle": 0},
                        {"time": 0.1, "angle": 70},
                        {"time": 0.5, "angle": 70},
                        {"time": 0.6, "angle": 0}
                    ]
                },
                "hair": {
                    "rotate": [
                        {"time": 0, "angle": 0},
                        {"time": 0.1, "angle": 30},
                        {"time": 0.3, "angle": 25},
                        {"time": 0.5, "angle": 30},
                        {"time": 0.6, "angle": 0}
                    ]
                },
                "dress_bottom": {
                    "rotate": [
                        {"time": 0, "angle": 0},
                        {"time": 0.1, "angle": 20},
                        {"time": 0.5, "angle": 20},
                        {"time": 0.6, "angle": 0}
                    ]
                }
            }
        },
        "magic": {
            "bones": {
                "spine2": {
                    "rotate": [
                        {"time": 0, "angle": 0},
                        {"time": 0.2, "angle": -10},
                        {"time": 0.5, "angle": 10},
                        {"time": 0.8, "angle": 0}
                    ]
                },
                "upper_arm_l": {
                    "rotate": [
                        {"time": 0, "angle": 0},
                        {"time": 0.2, "angle": -60},
                        {"time": 0.4, "angle": -120},
                        {"time": 0.6, "angle": -90},
                        {"time": 0.8, "angle": 0}
                    ]
                },
                "upper_arm_r": {
                    "rotate": [
                        {"time": 0, "angle": 0},
                        {"time": 0.2, "angle": 60},
                        {"time": 0.4, "angle": 120},
                        {"time": 0.6, "angle": 90},
                        {"time": 0.8, "angle": 0}
                    ]
                },
                "hair": {
                    "rotate": [
                        {"time": 0, "angle": 0},
                        {"time": 0.3, "angle": -20},
                        {"time": 0.5, "angle": 20},
                        {"time": 0.8, "angle": 0}
                    ]
                },
                "dress_bottom": {
                    "rotate": [
                        {"time": 0, "angle": 0},
                        {"time": 0.3, "angle": -15},
                        {"time": 0.5, "angle": 15},
                        {"time": 0.8, "angle": 0}
                    ]
                }
            }
        }
    }
}

# Write Spine JSON
spine_path = os.path.join(SPINE_DIR, "aelora_skeleton.json")
with open(spine_path, "w") as f:
    json.dump(spine_data, f, indent=2)
print(f"Created Spine skeleton: {spine_path}")

# Create a simple texture atlas file
atlas_content = """aelora.png
size: 512, 512
filter: Linear, Linear
head
  xy: 0, 0
  size: 80, 90
  orig: 80, 90
  offset: 0, 0
hair
  xy: 80, 0
  size: 100, 120
  orig: 100, 120
  offset: 0, 0
torso
  xy: 180, 0
  size: 60, 80
  orig: 60, 80
  offset: 0, 0
dress_upper
  xy: 240, 0
  size: 70, 60
  orig: 70, 60
  offset: 0, 0
dress_lower
  xy: 310, 0
  size: 120, 100
  orig: 120, 100
  offset: 0, 0
upper_arm_l
  xy: 0, 120
  size: 25, 55
  orig: 25, 55
  offset: 0, 0
upper_arm_r
  xy: 25, 120
  size: 25, 55
  orig: 25, 55
  offset: 0, 0
lower_arm_l
  xy: 50, 120
  size: 20, 50
  orig: 20, 50
  offset: 0, 0
lower_arm_r
  xy: 70, 120
  size: 20, 50
  orig: 20, 50
  offset: 0, 0
hand_l
  xy: 90, 120
  size: 22, 22
  orig: 22, 22
  offset: 0, 0
hand_r
  xy: 112, 120
  size: 22, 22
  orig: 22, 22
  offset: 0, 0
upper_leg_l
  xy: 134, 120
  size: 28, 60
  orig: 28, 60
  offset: 0, 0
upper_leg_r
  xy: 162, 120
  size: 28, 60
  orig: 28, 60
  offset: 0, 0
lower_leg_l
  xy: 190, 120
  size: 22, 55
  orig: 22, 55
  offset: 0, 0
lower_leg_r
  xy: 212, 120
  size: 22, 55
  orig: 22, 55
  offset: 0, 0
foot_l
  xy: 234, 120
  size: 30, 18
  orig: 30, 18
  offset: 0, 0
foot_r
  xy: 264, 120
  size: 30, 18
  orig: 30, 18
  offset: 0, 0
sparkle
  xy: 294, 120
  size: 20, 20
  orig: 20, 20
  offset: 0, 0
"""

atlas_path = os.path.join(SPINE_DIR, "aelora.atlas")
with open(atlas_path, "w") as f:
    f.write(atlas_content)
print(f"Created atlas: {atlas_path}")

# Pack all parts into a single texture atlas PNG
atlas_img = Image.new("RGBA", (512, 512), (0, 0, 0, 0))
part_positions = {
    "head": (0, 0), "hair": (80, 0), "torso": (180, 0),
    "dress_upper": (240, 0), "dress_lower": (310, 0),
    "upper_arm_l": (0, 120), "upper_arm_r": (25, 120),
    "lower_arm_l": (50, 120), "lower_arm_r": (70, 120),
    "hand_l": (90, 120), "hand_r": (112, 120),
    "upper_leg_l": (134, 120), "upper_leg_r": (162, 120),
    "lower_leg_l": (190, 120), "lower_leg_r": (212, 120),
    "foot_l": (234, 120), "foot_r": (264, 120),
    "sparkle": (294, 120)
}

for name, pos in part_positions.items():
    part_path = os.path.join(OUTPUT_DIR, f"{name}.png")
    if os.path.exists(part_path):
        part = Image.open(part_path)
        atlas_img.paste(part, pos, part)

atlas_img_path = os.path.join(SPINE_DIR, "aelora.png")
atlas_img.save(atlas_img_path)
print(f"Created atlas texture: {atlas_img_path}")

print("\nDone! Spine skeleton with 5 animations created:")
print("  - idle (breathing, gentle sway)")
print("  - run (full run cycle with arm/leg swing)")
print("  - jump (leap with arms up)")
print("  - slide (low crouch slide)")
print("  - magic (arms raised casting)")
