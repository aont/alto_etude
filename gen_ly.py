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

sys.stdout.write('''\\version \"2.16.0\"
{
  \\clef alto
''')
for measure in range(100):
  sys.stdout.write("  ")
  for beat in range(4):
    n_note = random.randint(note_num_min, note_num_max)
    # sys.stdout.write("%s " % notes[n_note])
    sys.stdout.write("%s " % get_note(n_note))
  sys.stdout.write("\n")

sys.stdout.write('}\n')