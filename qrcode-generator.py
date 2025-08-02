import os
import qrcode
import hashlib

domain = "https://thesublimehouseevent.vn"
start_uid = 1
end_uid = 500

os.makedirs("qr_codes", exist_ok=True)

for i in range(start_uid, end_uid + 1):
    
    uid = f"{i:03d}" # Format the uid to be 3 digits long
    hash_uid = hashlib.md5(uid.encode()).hexdigest() # Hash the uid
    url = f"{domain}?uid={hash_uid}" # Create the url with the uid
    
    # Create the QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url) # Add the url to the QR code
    qr.make(fit=True) # Make the QR code fit the data

    img = qr.make_image(fill_color="black", back_color="white") # Create the image
    img.save(f"qr_codes/{uid}.png") # Save the image
    print(f"Generated QR code for {url} --> qr_codes/{uid}.png")

print("All QR codes generated successfully.")