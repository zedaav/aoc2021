import logging
from typing import List, Tuple

import numpy


class ImageProcessor:
    def __init__(self, algo: List[bool], image: List[List[bool]]):
        self.algo = numpy.array(algo).reshape([2] * 9)  # Reshape to a 9D array, so that it can be accessed by 9D tuples, e.g. (0,1,0,0,1,0,1,0,0)
        self.image = numpy.array(image)
        logging.debug(f"Initial image:\n{self.image}")

    @property
    def pixels(self) -> int:
        return numpy.count_nonzero(self.image)

    def process(self, iterations: int):
        # Before first process, all pixels out of the frame are 0s
        pad = 0

        # Iterate on process occurrences
        for _ in range(iterations):
            # New image with padded borders
            new_image = numpy.pad(self.image, 1, constant_values=pad)

            # Temporary image with additional border to handle N+3 segments on borders
            tmp_image = numpy.pad(new_image, 1, constant_values=pad)

            # Iterate an all pixels of new image
            for y in range(len(new_image)):
                for x in range(len(new_image[0])):
                    # Extract 3x3 segment
                    segment = tmp_image[x : x + 3, y : y + 3]

                    # Get new value from algo
                    new_image[x, y] = self.algo[tuple(segment.flatten())]

            # Next iteration padding; pixels out of the frame may become:
            # - 1s everywhere if there are 0s everywhere and algo[0]==1
            # - 0s everywhere if there are 1s everywhere and algo[1]==0
            #   (should be always the case, otherwise there will be an infinite number of 1s after 1st process iteration)
            pad = self.algo[(pad,) * 9]

            # New image after process
            self.image = new_image
            logging.debug(f"Image after process:\n{self.image}")


def parse_instructions(lines: List[str]) -> Tuple[List[int], List[List[int]]]:
    # First line is algorithm
    algo = [1 if c == "#" else 0 for c in lines[0]]

    # Browse remaining lines to build image
    image = []
    for line in filter(len, lines[1:]):
        image.append([1 if c == "#" else 0 for c in line])

    return ImageProcessor(algo, image)
