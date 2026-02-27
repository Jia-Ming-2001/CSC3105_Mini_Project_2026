import uwb_dataset
	
# import raw data
data = uwb_dataset.import_from_files()
	
# divide CIR by RX preable count (get CIR of single preamble pulse)
# item[2] represents number of acquired preamble symbols
for item in data:
	item[15:] = item[15:]/float(item[2])
	
print(data)