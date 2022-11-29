from music21 import *
from music21.note import Note 
import random
import numpy as np
from progress.bar import IncrementalBar

'''
Dictionary for representing major keys table
'''
MAJOR_KEYS = {
    'C': ['C', 'd', 'e', 'F', 'G', 'a', 'B'],
    'C#': ['C#', 'd#', 'e#', 'F#', 'G#', 'a#', 'B#'],
    'D': ['D', 'e', 'f#', 'G', 'A', 'b', 'C#'],
    'D#': ['D#', 'f', 'g', 'G#', 'A#', 'c', 'D'],
    'E': ['E', 'f#', 'g#', 'A', 'B', 'c#', 'D#'],
    'F': ['F', 'g', 'a', 'A#', 'C', 'd', 'E'],
    'F#': ['F#', 'g#', 'a#', 'B', 'C#', 'd#', 'E#'],
    'G': ['G', 'a', 'b', 'C', 'D', 'E', 'f#'],
    'G#': ['G#', 'a#', 'b#', 'C#', 'D#', 'e#', 'G'],
    'A': ['A', 'b', 'c#', 'D', 'E', 'f#', 'G#'],
    'A#': ['A#', 'c', 'd', 'D#', 'F', 'g', 'A'],
    'B': ['B', 'c#', 'd#', 'E', 'F#', 'g#', 'A#']
}

'''
Dictionary for representing minor keys table
'''
MINOR_KEYS = {
    'c': ['c', 'D', 'D#', 'f', 'b', 'G#', 'A#'],
    'c#': ['c#', 'D#', 'E', 'f#', 'g#', 'A', 'B'],
    'd': ['d', 'E', 'F', 'g', 'a', 'A#', 'C'],
    'd#': ['d#', 'E#', 'F#', 'g#', 'a#', 'B', 'C#'],
    'e': ['e', 'F#', 'G', 'a', 'b', 'C', 'D'],
    'f': ['f', 'G', 'G#', 'a#', 'c', 'C#', 'D#'],
    'f#': ['f#', 'G#', 'A', 'b', 'c#', 'D', 'E'],
    'g': ['g', 'A', 'A#', 'c', 'd', 'D#', 'F'],
    'g#': ['g#', 'A#', 'B', 'c#', 'd#', 'E', 'F#'],
    'a': ['a', 'B', 'C', 'd', 'e', 'F', 'G'],
    'a#': ['a#', 'B#', 'C#', 'd#', 'e#', 'F#', 'G#'],
    'b': ['b', 'C#', 'D', 'e', 'f#', 'G', 'A']
}

'''
Array representing all notes on the keyboard
'''
NOTES = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#','A', 'A#', 'B']

'''
Function for checking if the given note is minor

:param note: (str) Given note

:return: (bool) true - if given note is minor. False otherwise
'''
def is_minor(note: str) -> bool:
    return note not in NOTES

'''
Function for checking if the given note is major

:param note: (str) Given note

:return: (bool) true - if given note is major. False otherwise
'''
def is_major(note: str) -> bool:
    return not is_minor(note)

'''
Function for getting major chord from the given note

:param initial_note: (str) Given note from which we will construct a chord
:param octave: (int) In which octave will be chord

:return: (chord.Chord) Given chord object
'''
def get_major(initial_note: str, octave: int) -> chord.Chord:
    return chord.Chord([note.Note(initial_note.upper() + str(octave - 1)), note.Note(NOTES[(NOTES.index(initial_note.upper()) + 4) % len(NOTES)] + str(octave - 1)), note.Note(NOTES[(NOTES.index(initial_note.upper()) + 7) % len(NOTES)] + str(octave - 1))])

'''
Function for getting minor chord from the given note

:param initial_note: (str) Given note from which we will construct a chord
:param octave: (int) In which octave will be chord

:return: (chord.Chord) Given chord object
'''
def get_minor(initial_note: str, octave: int) -> chord.Chord:
    return chord.Chord([note.Note(initial_note.upper() + str(octave - 1)), note.Note(NOTES[(NOTES.index(initial_note.upper()) + 3) % len(NOTES)] + str(octave - 1)), note.Note(NOTES[(NOTES.index(initial_note.upper()) + 7) % len(NOTES)] + str(octave - 1))])

'''
Function for getting dim chord from the given note

:param initial_note: (str) Given note from which we will construct a chord
:param octave: (int) In which octave will be chord

:return: (chord.Chord) Given chord object
'''
def get_dim(initial_note: str, octave: int) -> chord.Chord:
    return chord.Chord([note.Note(initial_note.upper() + str(octave - 1)), note.Note(NOTES[(NOTES.index(initial_note.upper()) + 3) % len(NOTES)] + str(octave - 1)), note.Note(NOTES[(NOTES.index(initial_note.upper()) + 6) % len(NOTES)] + str(octave - 1))])

'''
Function for getting sus2 chord from the given note

:param initial_note: (str) Given note from which we will construct a chord
:param octave: (int) In which octave will be chord

:return: (chord.Chord) Given chord object
'''
def get_sus2(initial_note: str, octave: int) -> chord.Chord:
    return chord.Chord([note.Note(initial_note.upper() + str(octave - 1)), note.Note(NOTES[(NOTES.index(initial_note.upper()) + 2) % len(NOTES)] + str(octave - 1)), note.Note(NOTES[(NOTES.index(initial_note.upper()) + 7) % len(NOTES)] + str(octave - 1))])

'''
Function for getting sus4 chord from the given note

:param initial_note: (str) Given note from which we will construct a chord
:param octave: (int) In which octave will be chord

:return: (chord.Chord) Given chord object
'''
def get_sus4(initial_note: str, octave: int) -> chord.Chord:
    return chord.Chord([note.Note(initial_note.upper() + str(octave - 1)), note.Note(NOTES[(NOTES.index(initial_note.upper()) + 5) % len(NOTES)] + str(octave - 1)), note.Note(NOTES[(NOTES.index(initial_note.upper()) + 7) % len(NOTES)] + str(octave - 1))])

'''
Function for getting needed number of chords for the music

:param input_file: (stream.base.Score) parsed input file

:return: (int) Number of quarters needed
'''
def get_number_of_needed_chords(input_file: stream.base.Score) -> int:
    return len(input_file.parts[0]) * 4

'''
Function for getting random accomponiment

:param chords_num: (stream.base.Score) Number of needed chords in music
:param possible_combinations: (list[chord.Chord]) All possible combinations (keys corresponding) of chords (sus2, sus4, major, minor, dim)

:return: (list[chord.Chord]) New random accomponiment for the music
'''
def initial_population(chords_number: int, possible_combinations: list[chord.Chord]) -> list[chord.Chord]:
    accomponiment = []
    for i in range(chords_number):
        chord = random.choice(possible_combinations)
        accomponiment.append(chord)
    return accomponiment

'''
Function for generating all possible chords

:param music_key: (str) Key of the music to generate only corresponding to the table chords
:param octave: (int) In whic octave should be future chords 

:return: (list[chord.Chord]) New random accomponiment for the music
'''
def generate_all_possible_chords(music_key: str, octave: int) -> list[chord.Chord]:
    possible_combinations = []
    if music_key in MAJOR_KEYS.keys():
        for note_num in range(len(MAJOR_KEYS[music_key])):
            if (note_num != 7):
                if (is_major(MAJOR_KEYS[music_key][note_num])):
                    possible_combinations.append(get_major(MAJOR_KEYS[music_key][note_num], octave))
                elif (is_minor(MAJOR_KEYS[music_key][note_num])):
                    possible_combinations.append(get_minor(MAJOR_KEYS[music_key][note_num], octave))
            elif (note_num == 7):
                possible_combinations.append(get_dim(MAJOR_KEYS[music_key][note_num], octave))
            if (note_num != 3 and note_num != 7):
                possible_combinations.append(get_sus2(MAJOR_KEYS[music_key][note_num], octave))
            if (note_num != 4 and note_num != 7):
                possible_combinations.append(get_sus4(MAJOR_KEYS[music_key][note_num], octave))
    else:
        for note_num in range(len(MINOR_KEYS[music_key])):
            if (note_num != 2):
                if (is_major(MINOR_KEYS[music_key][note_num])):
                    possible_combinations.append(get_major(MINOR_KEYS[music_key][note_num], octave))
                elif (is_minor(MINOR_KEYS[music_key][note_num])):
                    possible_combinations.append(get_minor(MINOR_KEYS[music_key][note_num], octave))
            elif (note_num == 2):
                possible_combinations.append(get_dim(MINOR_KEYS[music_key][note_num], octave))
            if (note_num != 2 and note_num != 5):
                possible_combinations.append(get_sus2(MINOR_KEYS[music_key][note_num], octave))
            if (note_num != 2 and note_num != 6):
                possible_combinations.append(get_sus4(MINOR_KEYS[music_key][note_num], octave))
    return possible_combinations


'''
Function for creating new population of the evolutionary algorithm

:param population: (list[list[chord.Chord]]) Old population which should be considered
:param fit_result: (list[float]) Result of the fitness function for the given population
:param precet_offsprings: (float) How many precent of offsprings should be from the given population

:return: (list[chord.Chord]) New random accomponiment for the music
'''
def make_new_population(population: list[list[chord.Chord]], fit_result: list[float], precet_offsprings: float) -> list[list[chord.Chord]]:
    population = population.copy()
    fit_result = fit_result.copy()
    overall_fit = np.array(fit_result).sum()
    new_population = []
    probabilities = [i / overall_fit for i in fit_result]
    for i in range(int(len(population) * 0.01 * precet_offsprings)):
        parent1_index = np.random.choice(len(population), p=probabilities)
        parent1 = population[parent1_index]
        del population[parent1_index]
        del probabilities[parent1_index]
        overall_fit -= fit_result[parent1_index]
        del fit_result[parent1_index]
        probabilities = [i / overall_fit for i in fit_result]
        parent2_index = np.random.choice(len(population), p=probabilities)
        parent2 = population[parent2_index]
        del population[parent2_index]
        overall_fit -= fit_result[parent2_index]
        del fit_result[parent2_index]
        del probabilities[parent2_index]
        probabilities = [i / overall_fit for i in fit_result]
        new_population.append(mutation(crossover(parent1, parent2)))
    return new_population

'''
Function for sorting population by the given fitness_score

:param population: (list[list[chord.Chord]]) Population for sorting
:param fit_result: (list[float]) Result of the fitness function for each chromosome inside the population

:return: tupple(list[chord.Chord], list[float]) Sorted population and corresponding array of the fitness function of each chromosome
'''
def sort_population(population: list[list[chord.Chord]], fitness_score: list[float]):
    fitness_score = np.array(fitness_score)
    args = fitness_score.argsort()
    population = [population[i] for i in args]
    fitness_score = fitness_score[args]
    return population, fitness_score.tolist()

'''
Main function which represents evolutionary algorithm itself

:param chords_number: (int) Number of needed chords
:param possible_chords: (list[chord.Chord]) All possible chords for the given key of melody
:param melody: (stream.base.Score) Melody itself
:param population_size: (int) Size of the population on each generation
:param precent_offsprings: (int) Value of the offsprings on each iteration
:param generations: (int) Number of overall generations

:return: list[chord.Chord] Sorted population and corresponding array of the fitness function of each chromosome
'''
def evolution(chords_number: int, possible_chords: list[chord.Chord], melody: stream.base.Score, population_size = 200, precent_offsprings = 10, generations = 5000) -> list[chord.Chord]:
    bar = IncrementalBar("Evolutionary algorithm", max = generations)
    population = []
    for i in range(population_size):
        population.append(initial_population(chords_number, possible_chords))
    fit_result = [0] * population_size
    for chromosome_number in range(len(population)):
        fit_result[chromosome_number] = fitness_function(population[chromosome_number], melody)
    for generation in range(generations):
        childs = make_new_population(population, fit_result, precent_offsprings)
        fit_of_new_pop = [fitness_function(i, melody) for i in childs]
        childs, fit_of_new_pop = sort_population(childs, fit_of_new_pop)
        population, fit_result = sort_population(population, fit_result)
        counter = 0
        for i in range(len(fit_of_new_pop)):
            if fit_of_new_pop[i] > fit_result[counter]:
                fit_result[counter] = fit_of_new_pop[i]
                population[counter] = childs[i]
        bar.next()
    result, fit = sort_population(population, fit_result)
    bar.finish()
    return result[-1]

'''
Function for calculating fitness result of the given sample

:param generation: (int) Number of needed chords
:param possible_chords: (list[chord.Chord]) All possible chords for the given key of melody
:param melody: (stream.base.Score) Melody itself

:return: (float) Fitness of the given sample
'''
def fitness_function(generation: list[list[chord.Chord]], melody: stream.base.Score) -> float:
    time = 0 
    fitness_score = 0
    index_chord = 0
    p_chord = ""
    pp_chord = ""
    for melody_note in melody:
        if time >= 1:
            time = 0
            index_chord += 1
        if melody_note.isRest:
            continue
        for chord_note in generation[index_chord]:
            if pp_chord != "":
                if p_chord == pp_chord and p_chord != chord:
                    fitness_score += 800
            pp_chord = p_chord
            p_chord = chord_note
            if melody_note.name == chord_note.name:
                fitness_score += 8000 * melody_note.duration.quarterLength
            difference = abs(melody_note.pitch.midi % 12 - chord_note.pitch.midi % 12) % 13
            #HIGH POINTS
            if (difference == 0):
                fitness_score += 6000 * melody_note.duration.quarterLength
            elif (difference == 12):
                fitness_score += 4000 * melody_note.duration.quarterLength
            elif (difference == 7):
                fitness_score += 1400 * melody_note.duration.quarterLength
            elif (difference == 5):
                fitness_score += 1300 * melody_note.duration.quarterLength
            #MIDDLE POINTS
            elif (difference == 4):
                fitness_score += 1100 * melody_note.duration.quarterLength
            elif (difference == 3):
                fitness_score += 1100 * melody_note.duration.quarterLength
            elif (difference == 9):
                fitness_score += 1100 * melody_note.duration.quarterLength
            elif (difference == 8):
                fitness_score += 1100 * melody_note.duration.quarterLength
            #BAD_THING
            elif (difference == 2):
                fitness_score += 600 * melody_note.duration.quarterLength
            elif (difference == 10):
                fitness_score += 600 * melody_note.duration.quarterLength
            #VERY_BAD
            elif (difference == 11):
                fitness_score -= 0 * melody_note.duration.quarterLength
            elif (difference == 1):
                fitness_score -= 0 * melody_note.duration.quarterLength
            #DON'T DO THIS!!!
            elif (difference == 6):
                fitness_score -= 0 * melody_note.duration.quarterLength
        time += melody_note.duration.quarterLength
    return fitness_score

'''
Function for implementing crossover operation during evolutionary algorithm

:param father_chromosome: (list[list[chord.Chord]]) Father of the new chromosome (contains accomponiment)
:param mother_chromosome: (list[list[chord.Chord]]) Mother of the new chromosome (contains accomponiment)

:return: (list[list[chord.Chord]]) Child chromosome after crossover (contains accomponiment)
'''
def crossover(father_chromosome: list[list[chord.Chord]], mother_chromosome: list[list[chord.Chord]]) -> list[list[chord.Chord]]:
    new_child = []
    for i in range(len(father_chromosome)):
        new_child.append(random.choice([father_chromosome[i], mother_chromosome[i]]))
    return new_child

'''
Function for implementing crossover operation during evolutionary algorithm

:param chromosome: (list[list[chord.Chord]]) Father of the new chromosome (contains accomponiment)

:return: (list[list[chord.Chord]]) New chromosome after mutation
'''
def mutation(chromosome: list[list[chord.Chord]]) -> list[list[chord.Chord]]:
    global music_key
    global octave_mid
    random_chords = generate_all_possible_chords(music_key, octave_mid)
    for i in range(len(chromosome)):
        if random.randint(0, 100) < 10:
            chromosome[i] = random.choice(random_chords)
    return chromosome


'''
Name of the input file
'''
try:
    FILE_NAME = input(("Please, specify input file (it should be in the same package as py file or specify global path): "))
    OUTPUT_FILE = "".join(FILE_NAME.split('.')[:-1]) + "_with_accompaniment.mid"
    # try:
    initial_music = converter.parse(FILE_NAME)
    music_key = initial_music.analyze('key') #Parsing given midiFile
    composition = []
    octave = 0
    num_of_notes = 0
    for i in initial_music: # take all notes from the melody 
        counter = 0
        if type(i) == metadata.Metadata:
            continue
        for j in i: 
            for note_ in j.elements:
                if isinstance(note_, note.GeneralNote) != True:
                    continue
                composition.append(note_)
                if not(note_.isRest):
                    counter += note_.octave
                    num_of_notes += 1.
    octave_mid = int(counter / num_of_notes) # get median octave of the melody
    music_key = str(music_key).split()[0] # function for getting key of the melody and scale
    found_accomponiment = evolution(get_number_of_needed_chords(initial_music), generate_all_possible_chords(music_key, octave_mid), composition)
    #Last part is just generation of accomponiment and given melody
    output_music = stream.Stream()
    melodi = stream.Part()
    chords = stream.Part()
    for i in range(get_number_of_needed_chords(initial_music)):
        chords.append(chord.Chord(found_accomponiment[i]))
    for i in range(len(composition)):
        melodi.append(composition[i])
    melodi.insert(instrument.Vibraphone())
    chords.insert(instrument.Vibraphone())
    output_music.append(melodi)
    output_music.append(chords)
    output_music.write("midi", OUTPUT_FILE) 
    print("Your accomponiment was constructed!\nThe name of the file is:", OUTPUT_FILE)
except:
    print("Sory, but name of the file was wrong. Try next time!")