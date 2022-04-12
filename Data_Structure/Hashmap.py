class HashMap:
    def __init__(self, array_size):
        self.array_size = array_size
        self.array = [None for item in range(array_size)]

    def hash(self, key, count_collisions=0):
        key_bytes = key.encode()
        hash_code = sum(key_bytes)
        return hash_code + count_collisions

    def compressor(self, hash_code):
        return hash_code % self.array_size

    def get_array_value(self, key, number_collisions = 0):
        array_index = self.compressor(self.hash(key, number_collisions))
        return self.array[array_index], array_index

    def assign(self, key, value):
        current_array_value, array_index = self.get_array_value(key)
        if current_array_value is None:
            return

        if current_array_value[0] == key:
            self.array[array_index] = [key, value]
            return

    # Collision!

        number_collisions = 1

        while(current_array_value[0] != key):
            current_array_value, new_array_index = self.get_array_value(key, number_collisions)

            if current_array_value is None:
                self.array[new_array_index] = [key, value]
                return

            if current_array_value[0] == key:
                self.array[new_array_index] = [key, value]
                return

            number_collisions += 1
        
        return

    def retrieve(self, key):
   
        possible_return_value = self.get_array_value(key)

        if possible_return_value is None:
            return None

        if possible_return_value[0] == key:
            return possible_return_value[1]

        retrieval_collisions = 1

        while (possible_return_value != key):
      
            possible_return_value = self.get_array_value(key, retrieval_collisions)

            if possible_return_value is None:
                return None

            if possible_return_value[0] == key:
                return possible_return_value[1]

            retrieval_collisions += 1

        return