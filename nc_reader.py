import netCDF4 as nc

# Open the NetCDF file
nc_file = nc.Dataset('SODA_Salnity.nc', 'r')
nc_file2 = nc.Dataset('SODA_Temp.nc', 'r')

# Access a variable and its data
salnity_data = nc_file.variables['SALT'][:]
temp_data = nc_file2.variables['TEMP'][:]

output_file_name = 'Annual_variation_temp.txt'
output_file_name2 = 'Annual_variation_sal.txt'

def avg_2d(array):
    total_sum = 0
    element_count = 0

    # Iterate through the rows and columns of the 2D list
    for row in array:
        for element in row:
            total_sum += element
            element_count += 1

    # Calculate the average
    if element_count > 0:
        average = total_sum / element_count
    else:
        average = 0
    return average

# Open the output file in write mode
with open(output_file_name, 'w') as output_file:
    with open(output_file_name2, 'w') as output_file2:
        temp = 0
        sal = 0
        # output_file.write("Year,Month,Temperature,Salinity\n")
        for i in range(1680):
            temp += avg_2d(temp_data[i][0])
            sal += avg_2d(salnity_data[i][0])
            month = (i+1)%12
            if month==0:
                output_file.write(f"{i//12+1871}\t{temp/12}\n")
                output_file2.write(f"{i//12+1871}\t{sal/12}\n")
                sal = 0
                temp = 0
    # Write the data to the file
    # for value in temperature_data[:1]:
    #     for value1 in value:
    #         output_file.write(f"{value1}\n")

# Close the NetCDF file
nc_file.close()

print(f"Data has been written to {output_file_name}")