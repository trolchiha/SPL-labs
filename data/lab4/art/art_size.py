import numpy as np

class ArtSize:
    def __init__(self, width=5, height=5):
        self._width = width
        self._height = height
        self._chars = None

    def __str__(self):
        return f"Width: {self._width} \nHeight: {self._height}"

    def set_width(self, width):
        self._width = width

    def set_height(self, height):
        self._height = height

    def set_chars(self, chars):   
        self._chars = chars

    def get_resized_chars(self):
        resized_chars = []
        if self._chars is None:
            return "No chars to resize"
        for char in self._chars:
            resized_chars.append(self._change_char_size(char))
        
        self._chars = resized_chars
        return resized_chars
    
    def get_chars(self):
        return self._chars

    def _change_char_size(self, matrix):
        matrix = self._change_height(matrix)
        matrix = self._change_width(matrix)
        return matrix

    def _change_width(self, matrix):
        if self._width <= 5:
            return matrix
        
        columns_to_add = self._width-5
        column_index = round(len(matrix[0])/2)
        сolumn_to_add = [row[column_index] for row in matrix]
        np_matrix = np.array(matrix)
        
        for i in range(columns_to_add):
            np_matrix = np.insert(np_matrix, column_index, сolumn_to_add, axis=1)

        matrix = np_matrix.tolist()
        return matrix

    def _change_height(self, matrix):
        if self._height <= 5:
            return matrix
        
        lines_to_add = round((self._height-5)/2)
        top_line = matrix[1]
        bottom_line = matrix[len(matrix) - 2]

        np_matrix = np.array(matrix)

        for i in range(lines_to_add):
            top_row_index = 1
            bottom_row_index = np_matrix.shape[0] - 1
            np_matrix = np.insert(np_matrix, top_row_index, top_line, axis=0)
            np_matrix = np.insert(np_matrix, bottom_row_index, bottom_line, axis=0)

        matrix = np_matrix.tolist()
        return matrix
    