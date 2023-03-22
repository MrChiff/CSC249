from HashTable import HashTable

# OpenAddressingBucket represents a bucket with a key and a value
class OpenAddressingBucket:
    def __init__(self, bucket_key = None, bucket_value = None):
        self.key = bucket_key
        self.value = bucket_value
    
    def isEmpty(self):
        if self is OpenAddressingBucket.EMPTY_SINCE_START:
            return True
        return self is OpenAddressingBucket.EMPTY_AFTER_REMOVAL

# Initialize two special bucket types: empty-since-start and empty-after-removal
OpenAddressingBucket.EMPTY_SINCE_START = OpenAddressingBucket()
OpenAddressingBucket.EMPTY_AFTER_REMOVAL = OpenAddressingBucket()

# OpenAddressingHashTable is a base class for an open addressing hash table
class OpenAddressingHashTable(HashTable):
    def __init__(self, initialCapacity):
        self.table = [OpenAddressingBucket.EMPTY_SINCE_START] * initialCapacity
    
    def probe(self, key, i):
        # Each derived class must implement
        pass

    # Inserts the specified key/value pair. If the key already exists, the 
    # corresponding value is updated. If inserted or updated, True is returned. 
    # If not inserted, then False is returned.   
    def insert(self, key, value):
        # Search for the key in the table. If found, update the bucket's value.
        for i in range(len(self.table)):
            bucket_index = self.probe(key, i)
            
            # An empty-since-start bucket implies the key is not in the table
            if self.table[bucket_index] is OpenAddressingBucket.EMPTY_SINCE_START:
                break
            
            if self.table[bucket_index] is not OpenAddressingBucket.EMPTY_AFTER_REMOVAL:
                # Check if the non-empty bucket has the key
                if key == self.table[bucket_index].key:
                    # Update the value
                    self.table[bucket_index].value = value
                    return True
        
        # The key is not in the table, so insert into first empty bucket
        for i in range(len(self.table)):
            bucket_index = self.probe(key, i)
            if self.table[bucket_index].isEmpty():
                self.table[bucket_index] = OpenAddressingBucket(key, value)
                return True
        
        return False # no empty bucket found

    # Searches for the specified key. If found, the key/value pair is removed 
    # from the hash table and True is returned. If not found, False is returned.   
    def remove(self, key):
        for i in range(len(self.table)):
            bucket_index = self.probe(key, i)
            
            # An empty-since-start bucket implies the key is not in the table
            if self.table[bucket_index] is OpenAddressingBucket.EMPTY_SINCE_START:
                return False
            
            if self.table[bucket_index] is not OpenAddressingBucket.EMPTY_AFTER_REMOVAL:
                # Check if the non-empty bucket has the key
                if key == self.table[bucket_index].key:
                   # Remove by setting the bucket to empty-after-removal
                   self.table[bucket_index] = OpenAddressingBucket.EMPTY_AFTER_REMOVAL
                   return True
        return False # key not found
   
    # Searches for the key, returning the corresponding value if found, null if 
    # not found.
    def search(self, key):
        for i in range(len(self.table)):
            bucket_index = self.probe(key, i)
            
            # An empty-since-start bucket implies the key is not in the table
            if self.table[bucket_index] is OpenAddressingBucket.EMPTY_SINCE_START:
                return None
            
            if self.table[bucket_index] is not OpenAddressingBucket.EMPTY_AFTER_REMOVAL:
                # Check if the non-empty bucket has the key
                if key == self.table[bucket_index].key:
                    return self.table[bucket_index].value
        
        return None # key not found
   
    def __str__(self):
        result = ""
        for i in range(len(self.table)):
            result += "%d: " % i
            if self.table[i] is OpenAddressingBucket.EMPTY_SINCE_START:
                result += "EMPTY_SINCE_START\n"
            elif self.table[i] is OpenAddressingBucket.EMPTY_AFTER_REMOVAL:
                result += "EMPTY_AFTER_REMOVAL\n"
            else:
                result += "%s, %s\n" % (self.table[i].key, self.table[i].value)
        return result