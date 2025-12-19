
import pandas as pd

data = {
    'Name': ['Test Hospital 1', 'Test Hospital 2'],
    'Departments': ['Cardiology, Neurology', 'Orthopedics, Pediatrics'],
    'Address': ['123 Main St', '456 Oak Ave'],
    'Website': ['http://test1.com', 'http://test2.com'],
    'PhoneNo': ['123-456-7890', '098-765-4321'],
    'CurrentStatus': ['Open', 'Closed'],
    'Image': ['image1.jpg', 'image2.jpg'],
    'Timings': ['9am-5pm', '10am-6pm'],
    'Latitude': [34.0522, 36.1699],
    'Longitude': [-118.2437, -115.1398]
}
df = pd.DataFrame(data)
df.to_excel('app/tests/test_files/hospitals.xlsx', index=False)
