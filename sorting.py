class Sorting:

    def __init__(self):
        self.list = None

    def bubble_sort(self, array):
        self.list = array

        for i in range(len(self.list)):
            swap = False
            for j in range(len(self.list) - 1):
                if self.list[j] > self.list[j + 1]:
                    temp = self.list[j+1]
                    self.list[j+1] = self.list[j]
                    self.list[j] = temp
                    swap = True

            if not swap:
                return self.list

        return self.list

    def selection_sort(self, array):
        self.list = array

        for i in range(len(self.list)):
            smallest_index = i
            for j in range(i + 1, len(self.list)):
                if self.list[j] < self.list[smallest_index]:
                    smallest_index = j
            self.list[i], self.list[smallest_index] = self.list[smallest_index], self.list[i]

        return self.list

    def insertion_sort(self, array):
        self.list = array

        for i in range(len(self.list)):
            temp = self.list[i]
            j = i

            while j > 0 and temp < self.list[j - 1]:
                self.list[j] = self.list[j - 1]
                j -= 1

            self.list[j] = temp

        return self.list

    def merge_sort(self, array):
        length = len(array)

        if length == 1:
            return array

        middle = length // 2
        left = array[0:middle]
        right = array[middle:length]

        return self._merge(self.merge_sort(left), self.merge_sort(right))

    def _merge(self, array1, array2):

        array = []

        left = 0
        right = 0

        while left < len(array1) and right < len(array2):
            if array1[left] <= array2[right]:
                array.append(array1[left])
                left += 1
            else:
                array.append(array2[right])
                right += 1

        if left < len(array1):
            array.extend(array1[left:])
        else:
            array.extend(array2[right:])

        return array


sorting = Sorting()
print(sorting.merge_sort([1, 5, 4, 10, 1, 11, 2, 100, 95, 90, 80, 60, 3]))
