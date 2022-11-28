def gen(res,ClientName,mobile,q,price):
    import os
    from InvoiceGenerator.api import Invoice,Item,Client,Provider,Creator
    from InvoiceGenerator.pdf import SimpleInvoice
    import random

    bank_acc = random.randint(2335,2999)
    bank_acc = str(bank_acc)+'-3324-3453-'+str(bank_acc)

    bank_code = random.randint(4506,5506)
    bank_code = str(bank_code)
    os.environ['INVOICE_LANG'] = 'en'
    client = Client('Name: {} Mobile: {}'.format(ClientName.get(),mobile.get()))
    provider = Provider("TEAM 02",bank_account = bank_acc,bank_code=bank_code)
    creator = Creator('TEAM_140_151_166_177 02')
    invoice = Invoice(client,provider,creator)

    for i in range(len(res)):
        print(res[i])
        invoice.add_item(Item(q[i],price[i],description=res[i]))

    invoice.currency = 'RS.'
    num = random.randint(10,50)
    invoice.number = str(num)+str(num)+str(num)

    docu = SimpleInvoice(invoice)
    pdf_n0 = random.randint(1,10)
    pdf_n0_str = str(pdf_n0)
    gen_pdf = pdf_n0_str+'.pdf'
    print(gen_pdf)
    docu.gen(gen_pdf,generate_qr_code=True) 