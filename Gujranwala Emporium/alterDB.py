import sqlite3

con = sqlite3.connect(database=r'marketing.db')
cur = con.cursor()

cur.execute("Update property set client_cnic=?,downPayment=?,totalInstallments=?"
",pricePerInstallment=?,discount=?,status=?,installmentPlan=?,possession=? where propertyID=?",
('',
 '',
 '',
 '',
 '',
 'Available',
 '',
 '',
 73))
con.commit()