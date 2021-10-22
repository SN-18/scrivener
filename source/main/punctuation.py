from punctuator import Punctuator
import os.path

class Punctuation:
    """
    A class used to add punctuation to transcripts

    ...

    Attributes
    ----------
    punct_model: object
        a ML model for adding puctuation to strings

    Methods
    -------
    add_punctuation_transcript:
        Adds punctuation to string
    """
    def __init__(self):
        """
        Parameters
        ----------
        youtube_url : str
            link of youtube video
        """

    @staticmethod
    def add_punctuation_transcript(transcription):
        """
        Using the generated transcript, add punctuation
        """
        # initialize the punctuator ML model
        punct_model = Punctuator(os.path.abspath("source/punct_model_full.pcl"))

        # Add punctuation to text
        punct_text = punct_model.punctuate(transcription)

        # replace punctuation errors, sometimes ML model will double up on punctuation, replace it such that there is
        # only one punctuation which is correct
        punct_text = punct_text.replace(',,', ',').replace('!,', '!').replace('.,', '.').replace('?,', '?')\
            .replace(',.', ',').replace('!.', '!').replace('..', '.').replace('?.', '?').replace('",', ',"')\
            .replace('".', '."').replace('"!', '!"').replace('"?', '?"')

        return punct_text