#Problem Statement:
#Given a string input representing the file system in the explained format, return the length of the longest absolute path to a file in the abstracted file system. If there is no file in the system, return 0.
#Difficulty level: Medium

class Solution(object):
    def lengthLongestPath(self, input):
        # Split the input into lines based on newline characters
        lines = input.split('\n')
        
        # Stack to keep track of the length of the path at each level
        current_path_length = [0]  # Initialize with 0 for the root directory
        max_length = 0  # To track the longest file path
        
        for line in lines:
            # Determine the current level of indentation (number of tabs)
            level = line.count('\t')
            # Remove the tabs to get the actual name of the directory/file
            name = line.lstrip('\t')
            
            # Update the path length at the current level
            current_path_length = current_path_length[:level + 1]  # Trim the stack to the correct depth
            current_path_length.append(current_path_length[-1] + len(name) + 1)  # +1 for the "/" separator
            
            # Check if this is a file (has a dot in the name)
            if '.' in name:
                # If it's a file, check if the current path is the longest
                max_length = max(max_length, current_path_length[-1] - 1)  # Subtract 1 to avoid trailing '/'
        
        return max_length
