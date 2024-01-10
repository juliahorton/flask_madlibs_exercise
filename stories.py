"""Madlibs Stories."""

class Story:
    """Madlibs story.

    To  make a story, pass in a list of part-of-speech prompts, followed by the text of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, prompt:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, prompts, text):
        """Create story with part-of-speech prompts and template text."""

        self.prompts = prompts
        self.template = text

    def generate(self, answers):
        """Substitute user-provided answers into text.

        Args:
            answers (dict): key/value pairs for each answer's part of speech and the word that the user chose for it in the form of {prompt: answer, prompt: answer, ...}

        Returns:
            str: the completed Madlib
        """

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text


# Here's a story to get you started


story = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)
