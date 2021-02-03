from reportlab.lib.units import inch
from Bio import SeqIO
from Bio.Graphics import GenomeDiagram
from PIL import Image, ImageFont, ImageDraw

record = SeqIO.read("Genome.gb", "genbank")
DNA = GenomeDiagram.Diagram()

# Inside Track
final_track = DNA.new_track(1)
insideTrack = final_track.new_set()

# Makes tracks
track1 = DNA.new_track(2, height=0.75)
track2 = DNA.new_track(3, height=0.75)
track3 = DNA.new_track(4, height=0.75)

# Initializes a set
track1_set = track1.new_set()
track2_set = track2.new_set()
track3_set = track3.new_set()

# Renumber the tracks and increased the number by one each step
DNA.renumber_tracks(low=1, step=1)

colidx = 0
col = ["red", "orange", "yellow", "green"]

# Fills up the tracks.
for feat in record.features:
    if feat.type == "gene":
        color = col[colidx % 4]
        if colidx % 3 == 0:
            track1_set.add_feature(feat, color=color, label=True, label_size=20, label_angle=-90)
        elif colidx % 3 == 1:
            track2_set.add_feature(feat, color=color, label=True, label_size=20, label_angle=-90)
        else:
            track3_set.add_feature(feat, color=color, label=True, label_size=20, label_angle=-90)
        insideTrack.add_feature(feat, color="black")
        colidx += 1

# Creating png with name Tomato_Curly_Stunt_Virus
DNA.draw(end=len(record), format="circular", pagesize=(25 * inch, 25 * inch), circular=True, start=0, circle_core=0.1)
DNA.write("ACM_Virus.png", "PNG")
image = Image.open("ACM_Virus.png")

draw = ImageDraw.Draw(image)
font = ImageFont.truetype("IndieFlower-Regular.ttf", 50)
draw.text((550, 75), "Tomato Curly Stunt Virus", (0, 0, 0), font=font)

image.save('ACM_Virus.png')
