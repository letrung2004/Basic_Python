import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Define the data
diameters = [4879, 12104, 12756, 6792, 142984, 120536, 51118, 49528]
index = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

# Create the Series
planet_diameters = pd.Series(diameters, index=index)

# Find the diameter of Earth
earth_diameter = planet_diameters["Earth"]
print("The diameter of Earth is:", earth_diameter, "km")

# 4. Lấy đường kính từ "Mercury" đến "Mars"
mercury_to_mars = planet_diameters["Mercury":"Mars"]
print(mercury_to_mars)

# 5. Lấy đường kính của "Earth", "Jupiter" và "Neptune"
selected_planets = planet_diameters[["Earth", "Jupiter", "Neptune"]]
print(selected_planets)

# 6. Thêm Pluto vào danh sách và cập nhật Series
diameters.append(2370)
index.append("Pluto")
planet_diameters = pd.Series(diameters, index=index)
print(planet_diameters)

# 7. Tạo DataFrame chứa thông tin về hành tinh
data = {
    "diameter": [4879, 12104, 12756, 6792, 142984, 120536, 51118, 49528, 2370],
    "avg_temp": [167, 464, 15, -65, -110, -140, -195, -200, -225],
    "gravity": [3.7, 8.9, 9.8, 3.7, 23.1, 9.0, 8.7, 11.0, 0.7]
}

# Định nghĩa chỉ mục là tên hành tinh
index = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"]

# Tạo DataFrame
planets = pd.DataFrame(data, index=index)

print(planets)

# 8. Lấy 3 hàng đầu tiên của DataFrame planets
print(planets.head(3))

# 9. Lấy 2 hàng cuối của DataFrame planets
print(planets.tail(2))

# 10. Lấy tên các cột của DataFrame planets
print(planets.columns)

# 11. Kiểm tra chỉ mục sau khi đã đặt theo tên hành tinh
print(planets.index)

# 12. Lấy cột gravity của tất cả hành tinh
print(planets["gravity"])

# 13. Lấy cả gravity và diameter của tất cả hành tinh
print(planets[["gravity", "diameter"]])

# 14. Lấy gravity của Earth bằng loc
print(planets.loc["Earth", "gravity"])

# 15. Lấy cả diameter và gravity của Earth
print(planets.loc["Earth", ["diameter", "gravity"]])

# 16. Lấy gravity và diameter từ Earth đến Saturn
print(planets.loc["Earth":"Saturn", ["gravity", "diameter"]])

# 17. Kiểm tra tất cả hành tinh có đường kính > 1000 không
print(planets["diameter"] > 1000)

# 18. Chọn tất cả hành tinh có đường kính > 100000
print(planets[planets["diameter"] > 100000])

# 19. Chọn tất cả hành tinh có avg_temp > 0 và gravity > 5
print(planets[(planets["avg_temp"] > 0) & (planets["gravity"] > 5)])

# 20. Sắp xếp đường kính theo thứ tự tăng dần
print(planets["diameter"].sort_values())

# 21. Sắp xếp đường kính theo thứ tự giảm dần
print(planets["diameter"].sort_values(ascending=False))

# 22. Sắp xếp DataFrame theo cột gravity giảm dần
print(planets.sort_values(by="gravity", ascending=False))

# 23. Sắp xếp giá trị trong hàng "Mercury"
print(planets.loc["Mercury"].sort_values())


# SAEBORN

# 2. Display names of datasets
dataset_names = sns.get_dataset_names()
print(dataset_names)

# 3. Load the "tips" dataset into a pandas DataFrame
tips = sns.load_dataset('tips')

# 4. Scatter plot showing bill amount (x-axis) and tip amount (y-axis)
sns.scatterplot(data=tips, x='total_bill', y='tip')
plt.show()

# 5. Modify font size and set style to darkgrid
sns.set_context("notebook", font_scale=1.2)
sns.set_style("darkgrid")
sns.scatterplot(data=tips, x='total_bill', y='tip')
plt.show()

# 6. Assign marker colors based on the "day" column
sns.scatterplot(data=tips, x='total_bill', y='tip', hue='day')
plt.show()

# 7. Set marker sizes based on the "size" column
sns.scatterplot(data=tips, x='total_bill', y='tip', size='size', sizes=(20, 200))
plt.show()

# 8. Split the plot into subplots based on the "time" column
sns.relplot(data=tips, x='total_bill', y='tip', col='time', kind='scatter')
plt.show()

# 9. Further subdivide the plot using the "sex" column
sns.relplot(data=tips, x='total_bill', y='tip', col='time', row='sex', kind='scatter')
plt.show()

