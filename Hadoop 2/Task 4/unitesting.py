
import sys
import unittest
from io import StringIO

def mapper_hw5(input): # mapper_hw5.py based function
    sys.stdin = StringIO(input) # reading string input
    output = StringIO() # setting output to StringgIO to get mapper_hw5() output
    sys.stdout = output # storing result into "output" 
    
    # mapper_hw5.py code:
    for line in sys.stdin: 
        line = line.strip()
        cols = line.split(",")
    
        if len(cols) == 6: 
            key = cols[1] # VICTIMIZATION_PRIMARY Data1
            value = "smaller_data1.csv," + ",".join(cols) # change to smaller data
        else:
            key = cols[4] # VICTIMIZATION_PRIMARY Data2
            value = "smaller_data2.csv," + ",".join(cols)  # change to smaller data
        print(key + "\t" + value)
    
    return output.getvalue() # retrieve entire content of the file


def reducer_hw5(input): # reducer_hw5.py based function
    sys.stdin = StringIO(input) # reading string input
    output = StringIO() # setting output to StringgIO to get reducer_hw5() output
    sys.stdout = output # storing result into "output" 
    
    # reducer_hw5.py code:
    current_key = None 
    data1_rows = [] 
    data2_rows = [] 

    for line in sys.stdin: 
        line = line.strip() 
        key, value = line.split("\t", 1) 
    
        if key != current_key: 
            if current_key is not None: 
                for row1 in data1_rows:
                    for row2 in data2_rows: 
                        print(row1 + "\t" + row2) 
                    
            # Let's reset.
            current_key = key
            data1_rows = []
            data2_rows = []
    
        dataset, row = value.split(",", 1)
        if dataset == "smaller_data1.csv": # smaller data1
            data1_rows.append(row) 
        elif dataset == "smaller_data2.csv": # smaller data2
            data2_rows.append(row) 

    # Repeate process
    if current_key is not None:
        for row1 in data1_rows:
            for row2 in data2_rows:
                print(row1 + "\t" + row2)
    
    return output.getvalue() # retrieve entire content of the file

class ScriptTestCase(unittest.TestCase):

    # Checking for mapper_hw5.py logic using data1.csv
    # extract the value from VICTIMIZATION_PRIMARY as the key
    # return the name of "dataset1.csv" AND the orginal line as the value using comma as a seprator
    def test_mapper_hw5_data1(self): # test case 1
        line_data1 = "6/30/2003,CRIMINAL SEXUAL ASSAULT,0-19,F,WWH,42" 
        result = mapper_hw5(line_data1)
        expected = "CRIMINAL SEXUAL ASSAULT\tsmaller_data1.csv,6/30/2003,CRIMINAL SEXUAL ASSAULT,0-19,F,WWH,42\n"
        self.assertEqual(result, expected) # result must match expected

    # Checking for mapper_hw5.py logic using data2.csv
    # extract the value from VICTIMIZATION_PRIMARY as the key
    # return the name of "dataset2.csv" AND the orginal line as the value using comma as a seprator
    def test_mapper_hw5_data2(self): # test case 2
        line_data2 = "2/12/2023 17:57,400 E 83RD ST,RESTAURANT,CHATHAM,HOMICIDE,20-29,M,BLK,YES" 
        result = mapper_hw5(line_data2)
        expected = "HOMICIDE\tsmaller_data2.csv,2/12/2023 17:57,400 E 83RD ST,RESTAURANT,CHATHAM,HOMICIDE,20-29,M,BLK,YES\n"
        self.assertEqual(result, expected) # result must match expected


    def test_reducer_hw5(self): # test case 3 -> testing for join results
        line_data1 = "9/30/2023,BATTERY,0-19,F,BLK,25"
        line_data2 = "4/8/2020 14:40,5400 W HIRSCH ST,STREET,AUSTIN,BATTERY,20-29,M,BLK,YES" 

        mapper_hw5_output = mapper_hw5(line_data1) + mapper_hw5(line_data2)
        result = reducer_hw5(mapper_hw5_output)
        expected = "9/30/2023,BATTERY,0-19,F,BLK,25\t4/8/2020 14:40,5400 W HIRSCH ST,STREET,AUSTIN,BATTERY,20-29,M,BLK,YES\n" # this is the result mapper_hw5.py and reducer_hw5.py returns
        self.assertEqual(result, expected) # result must match expected


    def test_reducer_hw5_non_matching(self): # test case 4 -> testing for non mtahcing results
        line_data1 = "3/31/2011,HOMICIDE,30-39,M,BLK,1"
        line_data2 = "1/13/2018 1:25,900 W 114TH PL,RESIDENCE,MORGAN PARK,BATTERY,0-19,M,BLK,YES" 
        
        mapper_hw5_output = mapper_hw5(line_data1) + mapper_hw5(line_data2)
        result = reducer_hw5(mapper_hw5_output)
        expected = "" # no output because line_data1 and line_data 2 don't match (it has to PASS)
        self.assertEqual(result, expected) # result must match expected
        
if __name__ == "__main__":
    unittest.main()
        
# cd ~/Desktop       
# python3 unitesting.py -> MAC terminal

# unittest: https://www.browserstack.com/guide/unit-testing-python
# StringIO: https://www.geeksforgeeks.org/stringio-module-in-python/
# Stack Overflow: https://stackoverflow.com/questions/2654834/capturing-stdout-within-the-same-process-in-python/3113913
# Stack Overflow: https://stackoverflow.com/questions/1218933/can-i-redirect-the-stdout-into-some-sort-of-string-buffer
# StringIO and getvalue(): https://wrongsideofmemphis.com/2010/03/01/store-standard-output-on-a-variable-in-python/
# unittest: https://blog.zhengdong.me/2012/07/30/streaming-python-unit-testing/
