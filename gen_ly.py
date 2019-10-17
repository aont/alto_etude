#!/usr/bin/env python
import random
import sys

random.seed(123456)

def get_note(note_num):
  q, mod = divmod(note_num, 7)
  return "cdefgab"[mod] + ['','\'', '\'\''][q] + "4"

# notes = []
# for octave in ['','\'', '\'\'']:
#   for note in "cdefgab":
#     notes.append(note+octave+"4")

note_num_min = 0
note_num_max = 7 * 2
delta_max = 5
sys.stdout.write('''\\version \"2.16.0\"
{
  \\clef alto
''')

n_note_prev = random.randint(note_num_min, note_num_max)
for measure in range(100):
  sys.stdout.write("  ")
  for beat in range(4):
    while True:
      delta = random.randint(-delta_max, delta_max)
      if delta==0:
        continue
      n_note = n_note_prev + delta
      if note_num_min <= n_note and n_note <= note_num_max:
        break      
    # sys.stdout.write("%s " % n_note)
    # sys.stdout.write("%s " % notes[n_note])
    sys.stdout.write("%s " % get_note(n_note))
    n_note_prev = n_note
  sys.stdout.write("\n")

# for t in range(30):
#   note_ary = list(range(note_num_min, note_num_max))
#   random.shuffle(note_ary)
#   sys.stdout.write("  ")
#   for n_note in note_ary:
#     sys.stdout.write("%s " % get_note(n_note))
#   sys.stdout.write("\n")

# for measure in range(100):
#   sys.stdout.write("  ")
#   for beat in range(4):
#     n_note = random.randint(note_num_min, note_num_max)
#     # sys.stdout.write("%s " % n_note)
#     # sys.stdout.write("%s " % notes[n_note])
#     # sys.stdout.write("%s " % get_note(n_note))
#   sys.stdout.write("\n")

sys.stdout.write('}\n')