BULK INSERT transactions
FROM 'C:\Users\herrl\source\pyrepos\.venvs\lambertfinance\outputfiles\combined_output.csv' -- Specify the full path to your CSV file
WITH
(
    FIELDTERMINATOR = ',', -- Specifies the character that separates fields in the CSV file
    ROWTERMINATOR = '\n',  -- Specifies the character that marks the end of a row
    FIRSTROW = 2,          -- Skips the header row if present (adjust if your CSV has no header or multiple header rows)
    CODEPAGE = 'RAW'       -- Specifies the code page of the data in the data file (adjust as needed for character encoding)
    -- Other optional parameters:
    -- BATCHSIZE = 10000,    -- Specifies the number of rows in a batch
    -- MAXERRORS = 10,       -- Specifies the maximum number of errors allowed before the bulk-import operation is canceled
    -- TABLOCK             -- Acquires a table-level lock for the duration of the bulk-import operation
);