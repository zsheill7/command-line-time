# if df.empty:
#     print("CSV is empty")
#     fields = [ 'date', 'time', 'activity', 'category']
#     with open(output_file_name, "w") as f:
#         w = csv.writer(f)
#         w.writerow(fields)

# with open("test_output.csv", "w") as f:
#     w = csv.writer( f )
#     w.writerow(fields)
#     times = list(record_dict.values())[0].keys()
#     for key in record_dict.keys():
#         w.writerow([key] + [record_dict[key][time] for time in times])