To create a Database => "CREATE DATABASE enery_meter";
To create a Table => "CREATE TABLE energy_data(r_no BIGINT(10) AUTO_INCREMENT, power FLOAT(10) ,price FLOAT(10) , time_tamp TIMESTAMP, PRIMARY KEY (r_no));"
To Insert data into Table => "INSERT INTO `energy_data` (`r_no`, `power`, `price`, `time_tamp`) VALUES (NULL, '2', '20', current_timestamp());"
To Update the Data => "UPDATE energy_data SET price=10 WHERE r_no=1;"
To Delete a record from Table=> "DELETE FROM energy_data WHERE r_no=3;"
To Select a record => "SELECT * FROM `energy_data` WHERE r_no=2;"
