import sys
import argparse
import librosa
import numpy as np
import matplotlib.pyplot as plt

def main(argv):
    argParser = argparse.ArgumentParser()
    argParser.add_argument('-f', '--file', help='The path to the audio file', required='True')

    args = argParser.parse_args()
    print(args.file)
    
    y, sr = librosa.core.load(args.file)
    spectrogram = librosa.feature.melspectrogram(y=y, sr=sr)
    spectrogram = librosa.power_to_db(spectrogram, ref=np.max)
    librosa.display.specshow(spectrogram, x_axis='time',
                                   y_axis='mel', sr=sr,
                                   fmax=8000)
    plt.colorbar()
    plt.set_cmap('hot_r')
    plt.show()

if __name__ == "__main__":
    main(sys.argv[1:])
