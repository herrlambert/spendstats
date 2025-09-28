CREATE TABLE transactions (
    transaction_date Date,
    category nvarchar(50),
    subcategory nvarchar(50),
    description nvarchar(100),
    debit_amount money,
    credit_amount money,
    card_user nvarchar(50)
);