#Parsing .pst file using pypff library

import pypff

pst = pypff.file()
pst.open("mails.pst")
root = pst.get_root_folder()

def parse_folder(base):
    messages = []
    for folder in base.sub_folders:
        if folder.number_of_sub_folders:
            messages += parse_folder(folder)
        print(folder.name)
        for message in folder.sub_messages:
            messages.append({
                "subject": message.subject,
                "sender": message.sender_name,
                "datetime": message.client_submit_time,
                "body": message.plain_text_body
            })
    return messages

messages = parse_folder(root)
