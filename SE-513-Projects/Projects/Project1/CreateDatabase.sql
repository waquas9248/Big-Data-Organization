JOIN
CREATE TABLE ClassDesc(
    LabelName VARCHAR(50),
	DisplayName VARCHAR(75),
    PRIMARY KEY (LabelName)
);

DROP TABLE IF EXISTS Human;
CREATE TABLE Human(
    ImageID VARCHAR(100),
    Source VARCHAR(25),
    LabelName VARCHAR(50),
    Confidence VARCHAR(10),
    PRIMARY KEY (ImageID, Source, LabelName, Confidence)
);

DROP TABLE IF EXISTS Machine;
CREATE TABLE Machine(
    ImageID VARCHAR(100),
    Source VARCHAR(25),
    LabelName VARCHAR(50),
    Confidence VARCHAR(10),
    PRIMARY KEY (ImageID, Source, LabelName, Confidence)
);

LOAD DATA LOCAL INFILE '/mnt/disks/Disk1/sql/class-descriptions.csv'
INTO TABLE ClassDesc
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(LabelName, DisplayName);

LOAD DATA LOCAL INFILE '/mnt/disks/Disk1/sql/human-imagelabels.csv'
INTO TABLE Human
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(ImageID, Source, LabelName, Confidence);

LOAD DATA LOCAL INFILE '/mnt/disks/Disk1/sql/machine-imagelabels.csv'
INTO TABLE Machine
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(ImageID, Source, LabelName, Confidence);

DROP TABLE IF EXISTS HumanClassDesc;
CREATE TABLE HumanClassDesc AS
SELECT Human.ImageID, Human.Source, Human.LabelName, Human.Confidence, ClassDesc.DisplayName
FROM Human
INNER JOIN ClassDesc
ON Human.LabelName = ClassDesc.LabelName;

DROP TABLE IF EXISTS MachineClassDesc;
CREATE TABLE MachineClassDesc AS
SELECT Machine.ImageID, Machine.Source, Machine.LabelName, Machine.Confidence, ClassDesc.DisplayName
FROM Machine
INNER JOIN ClassDesc
ON Machine.LabelName = ClassDesc.LabelName;


--Get most command displayname for table
SELECT DisplayName,
 COUNT(DisplayName)
FROM HumanClassDesc
GROUP BY  DisplayName
ORDER BY COUNT(DisplayName) ASC;

--Get most command displayname for table
SELECT DisplayName,
 COUNT(DisplayName)
FROM MachineClassDesc
GROUP BY  DisplayName
ORDER BY COUNT(DisplayName) ASC;

--Get the count for HumanClassDesc Table
SELECT 
    sum(case when DisplayName='Person' then 1 else 0 end) as PersonCount,
    sum(case when DisplayName='Sky' then 1 else 0 end) as SkyCount,
    sum(case when DisplayName='Tree' then 1 else 0 end) as TreeCount
FROM MachineClassDesc;

--Get the count for the MachineDescTable
SELECT 
    sum(case when DisplayName='Person' then 1 else 0 end) as PersonCount,
    sum(case when DisplayName='Sky' then 1 else 0 end) as SkyCount,
    sum(case when DisplayName='Tree' then 1 else 0 end) as TreeCount
FROM HumanClassDesc;

--Write HumanClassDesc to a csv
SELECT 'ImageID', 'Source', 'LabelName', 'Confidence', 'DisplayName'
UNION ALL
SELECT ImageID, Source, LabelName, Confidence, DisplayName
FROM HumanClassDesc
INTO OUTFILE '/mnt/disks/Disk1/sql/tables/HumanClassDesc.csv' 
FIELDS TERMINATED BY ',' 
LINES TERMINATED BY '\n';

--Write MachineClassDesc to a csv
SELECT 'ImageID', 'Source', 'LabelName', 'Confidence', 'DisplayName'
UNION ALL
SELECT ImageID, Source, LabelName, Confidence, DisplayName
FROM MachineClassDesc
INTO OUTFILE '/mnt/disks/Disk1/sql/tables/MachineClassDesc.csv' 
FIELDS TERMINATED BY ',' 
LINES TERMINATED BY '\n';