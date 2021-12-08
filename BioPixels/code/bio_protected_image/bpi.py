# kaspersky 
# Author: Ahmed Zakaria Mohamed
# Bio Protected Image

import hashlib
import cv2
import numpy 
from pathlib import Path
from PIL import Image 
import piexif

class bio_protected_image:
    
    #finger_template_dataset
    finger_templates = {'Heba':'0x5A4B46695801314B14AAE8014401435320F9F81776AB36AF1AAE32BE17EE28FE1FDC0EDE34D937A98DEB01A782ED03EF03AC03BB0F901798830F870F700F704F24E671EE2CCE68EE2C8B25AB2D232765003F0A7F178E178E0F870587870BBD0B86199D8799C3F9E3B924B9E8ECCC6DC23CB435D13BB636F05FE03FF0478387838F258F1D876F9F4D914B99CBB9D5B9E2B9DA39C70FC01DD16BE439F03BF43BB29B853792EE06EF0DE44AECA8BC017C02FB01BC43633138C1F1C1F0C37FC07FC3FA58A9F29B30AF307B26FF260C92BC90AC81AC110C381C5823294CC9638B65CBC3E6E3E639E1E363AF058B145F07570D7C86790F3987391F2C872D5D05712D991B23274B71C72143B3C3F363DF219D03EB22B781F9C4F980B981F9C13DADBC892E33251B66C3269376C63EC20EC736C3362336634F6257C3399AB5C1D59E9199C99A9199249B21BBE4D024B3DCAF6C369C237E027C077E4F0B0203090A11080108100705044BFF12021008C0660C0C090809150200010B0E23102009011483190C0703511B000313100301020203070503090602000A03060A000A3C66051245FF470309274B420B0A081E5B2111030006070E07080501092D0D070208160E0003831001011E020106020F070602020504051F0106578802032FE46A030505502B0705050B3E09020200090957150908021A120706031067130F0532310A031E0A01040101080506010D020647000831FF06071A3136010509050E0709080C4409060002121C4E480A0305245B1C0B020F521507073B1803030802010200050D0F0A000518085706070BAC01030A030B0303111A091518040B8711080A01150BFF5A0414030C030E04010B0A010201441501051D03040000010D0100000101000000010002020359610100024FFF63040001023186030000020101020404000200000200000001000000010000020102050201090801030901112200021814090159FF14040813F1670105080D161904010004141A171D070118861C1A08011116040106010000040003020100080504000401072D01041CA20108359C1B01081CAE3F0103021F5A230A000204177E250604001752130C030E23110403421902001202000A0004070501000408035504102CFF020D31282403021127202405021E98201406010F129A690608080B16150902050F040301150401001E02020300070901010102000336000101420200010B090000050C07060103031B040400010D53FF2C04140108487404000102020002010100010300060000000A0300000002000201020006000200000000007FED000603000CFFD505030005000A0400020000000000000000000000010000000C000101000003030100010304040001082D050623721E04082F7C1503060852FF40050000030413120301010E200902001A3F0A03009E2701005F09010B0005080502020402020E000337860B021ACC49000911390D03050731232304000208091409030004150C13070132AA1D07069C3E0702370501070107110000000406013202080E9901080B1D1D03010E2313060202164F120302010B1C5B2F01020231B326020028B14707064B4D070212040201000307020003020607090003000102000201000303034401010E020002070000001168CE030312002DFF8A0104031712000000000100000108010100130000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000',
    'Salma':'0x5A4B46695801314B14AAE8014401435320F9F8177E537E161A571E4F09DE1CFF51CE05DE2F6B27690F630D338B2380D7079E03CB278882CC8756071FF81BE85FB0CF70FB746B326B366B366B0AD518910C8F2B1F7F8E078EBF8E1787AE072E0F8439A51FF159F269F94031693C626D613EA438D14DF07AB01FCC1FB80F8B07A92647366F8E9F065F43CB03C971FB31E9B16219E73EE13CC937E83FF816E815981D9139937E2B3E0FBD242E1DDE012E03FB41BC43E361D8C771C4F9C37DC83DC8D5C141C9D781DB80BF12BF04BA0A3A9AE2A3BA1B262F324B0F270E8F45460D4B036625665BE34DE13F275B21DF147B12BA437A02B98FB00F322D333B03372B174C9749C722C70CC75B675CA38E215D27FA41FAC16E33FA40790EFA4B3A35B26BB2E332E359C368C27E861C827D155C376C8B6C85A6659E613B63BB619D2A2F670279237501F322D705D322D3179B1413788778177C03FC000D0106041F12040100020E0B0224910F07080FFF210A1A050C07120102000A19401B1D1F0111B92C0D0A032F1C00010B0601000501010100050B0A05020B04071201072D400E0D1DFF2E040F1C373006070A1E661D1703000C040708060306131F030C081670130203752702002E06001003090A0602000901093F0103469003022FB64203050E66230A0701101C0B0303000F0A622D0C03041A2D0F0A03154C1B05015B1F06021005010403040F0907030D060732020C29FD040D1729290505090F0B0E0A021243080A06031C1F3E310803063A68221302107630110F3312090212010103010307110300051B083802120F8F010B16111C0702184A1C2312021066230807021714FF4009140413081008000012050406300906022203000201060D000000000000010001050900003D7706000340FF300100020A4D6103020008010100000700052600010003030200010103010008020B020303060403010F06181A00041D22070A47FF1603090F7A490708081416170604000917181816060015AB231105095D1200061A1604000C05020D0205070806000E0103250002248A0608278727020D146C280304052234130C00010F145E180701032651130A0222641A0810642D03001C05000E010E070C04000406024802111EFF030A20252005012218151308050D90230F060210138658050804181617090010381008062F1A05001104030100020B0200000102014D0002004C00000001010000060C03010900033D090200001351FF47030C010B4964050001010808010102050205010B0100000E040000000204060302030600020712040205624410050A023EFF7C0704000E03480903070409050100000101000300290204023403060401000B030100000000010103010E02021C510900063C7A1E0504113CFF4F04010006080E0D040306213E0A00012C56110200903C0A024C0A04070105070401010802022C00091A750101247C16010B214C220103072242210301000B24862403000335402D05001C7D2D0901651906011A0101050100040300000301031E00010630000202151001020B160D040B0C24300E01020109225E1D0702075CFF3C020126A7780901343A090222040603020206070101010606070201050200011408010506066C12010C050710030200000F4F5302070E0040FF6804080418310400010101000105050103000A0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'}

    image_shape = (480, 640, 3)
    working_image = []
    selected_fp = ''

    def print_fin(self):
        print(self.finger_templates['Heba'])
    
    def sha1_hash(self,data):
        return hashlib.sha1(data.encode()).hexdigest()
    
    def sha256_hash(self,data):
        return hashlib.sha256(data.encode()).hexdigest()
    
    def capture_image(self):
        # define a video capture object
        vid = cv2.VideoCapture(0)
        image = []
        while(True):
            
            
            # Capture the video frame
            # by frame
            ret, frame = vid.read()
        
            # Display the resulting frame
            cv2.imshow('frame', frame)
            
            # the 'q' button is set as the
            # quitting button you may use any
            # desired button of your choice
            if cv2.waitKey(1) & 0xFF == ord('q'):
                image = frame
                break
        
        # After the loop release the cap object
        vid.release()
        # Destroy all the windows
        cv2.destroyAllWindows()
        
        return image

    def view_image(self,image):
        cv2.imshow('Captured_image',image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    
    def load_image(self,image):
        print('Captured Image Loaded To Working Varible')
        self.working_image = image

    def hash_to_ascii(self,hash):
        pixels = []
        for letter in hash:
            if letter.isalpha():
                #convert char to ascii
                pixels.append(ord(letter))
            else:
                pixels.append(int(letter))
        return pixels

    def hash_to_ascii_pixels(self,hash):
        pixels = []
        final_signature = []
        temp = []
        for letter in hash:
            if letter.isalpha():
                #convert char to ascii
                pixels.append(ord(letter))
            else:
                pixels.append(int(letter))
        
        counter = 0
        temp_counter = 0
        
        while counter < len(pixels):
            if temp_counter != 3:
                temp.append(pixels[counter])
                temp_counter += 1
            else:
                final_signature.append(temp)
                temp = []
                temp.append(pixels[counter])
                temp_counter = 1
            
            counter += 1 

        if len(temp) != 0:
            final_signature.append(temp) # ensure that taked every char of hash

        #check and complete final pixels
        index = len(final_signature)
        if len(final_signature[index - 1]) < 3:
            no = 3 - len(final_signature[index - 1])
            while no > 0:
                final_signature[index - 1].append(0)
                no -= 1
            
            #print(final_signature[index - 1])
        #self.view_image(final_signature)

        #print(pixels)
        #convert list to numpy array
        final_signature = numpy.array(final_signature , dtype=object)
        #print(final_signature)
        return final_signature

    def insert_hash(self,path,hash):
        im = Image.open(path)
        if "exif" in im.info:
            exif_dict = piexif.load(im.info["exif"])
            exif_dict["0th"][piexif.ImageIFD.ImageDescription] = hash
            exif_bytes = piexif.dump(exif_dict)
        else:
            exif_bytes = piexif.dump({"0th":{piexif.ImageIFD.ImageDescription:hash}})

        im.save(path, exif=exif_bytes)
        im.close()
        #rename file
        p = Path(path)
        p.rename(p.with_suffix('.bpi'))
        print(path,' -> Exported')


    def export_hash(self,path):
        im = Image.open(path)

        print(piexif.load(im.info["exif"])["0th"]\
            [piexif.ImageIFD.ImageDescription].decode("utf-8"))
        im.close()

    def export_file(self,image,fp):
        path = 'export/image.jpg'
        path2 = 'export/image.bpi'
        cv2.imwrite(path, image)
        self.insert_hash(path,fp)
        self.export_hash(path2)
    
    def export_bpi(self,data,hash):
        #new_edit
        name_of_image = str(input('Image Name: '))
        file_name = 'export/'+name_of_image+'.bpi'
        f = open(file_name, "a")
        f.write("data")
        f.write('\n')
        for corupted_pixel in data:
            f.write(str(corupted_pixel)+',')
        f.write('\n')
        f.write('Hash')
        f.write('\n')
        f.write(hash)
        f.close()

    def read_bpi(self):
        f = open("export/corupted_image.bpi", "r")
        lines = f.readlines()
        px_list = []
        bpi_owner_hash256 = ''
        #pixels at line 2
        #hash at line 4
        print('no of lines : ',len(lines))
        print('bpi owner hash : ',lines[3])
        bpi_owner_hash256 = lines[3]
        temp_px = lines[1]
        px_list = temp_px.split(',')
        px_list.remove(px_list[len(px_list)-1])
        
        return px_list
    
    def read_bpi_api(self,file_name):
        f = open(file_name, "r")
        lines = f.readlines()
        px_list = []
        bpi_owner_hash256 = ''
        #pixels at line 2
        #hash at line 4
        print('no of lines : ',len(lines))
        print('bpi owner hash : ',lines[3])
        bpi_owner_hash256 = lines[3]
        temp_px = lines[1]
        px_list = temp_px.split(',')
        px_list.remove(px_list[len(px_list)-1])
        
        return px_list,bpi_owner_hash256

    def create_key(self,hash1,hash2):
        key = []
        hash2_len = len(hash2)
        hash2_index = 0
        for x in hash1:
            if hash2_index == hash2_len:
                hash2_index = 0
            key.append(x+hash2[hash2_index])
            
            hash2_index += 1
        return key
    
    def corrupt_image(self,image,hash1,hash2):
        #key = hash2+hash1
        key = self.create_key(hash2,hash1)
        #new edit
        x_key = max(hash1) * min(hash1)
        key_len = len(key)
        index_of_key = 0
        self.image_shape =  image.shape
        print('X_data shape:', numpy.array(image).shape)
        px_list = []
        
        for list_pixels in image:
            for pixels in list_pixels:
                for px in pixels:
                    
                    if index_of_key == key_len:
                        index_of_key = 0
                    
                    key_value = key[index_of_key]
                    #edit
                    px_list.append((px + key_value) + x_key )
                    index_of_key += 1

        #print(px_list)
        #self.view_image(image)
        
        return px_list
    
    def reshape(self,data):
        px_list = numpy.array(data,dtype='uint8')
        px_list = numpy.reshape(px_list,self.image_shape)
        self.view_image(px_list)
              
    def uncorrupt_image(self,cor_image,hash1,hash2):
        key = self.create_key(hash2,hash1)
        #new edit
        x_key = max(hash1) * min(hash1)
        key_len = len(key)
        index_of_key = 0
        px_list = []
        for x in cor_image:
            if index_of_key == key_len:
                index_of_key = 0
            
            key_value = key[index_of_key]
            px_list.append((int(x) - key_value) - x_key )
            index_of_key +=1

        #px_list = numpy.asarray(px_list)
        #PIL_image = Image.fromarray(numpy.uint8(px_list)).convert('RGB')
        #PIL_image = Image.fromarray(px_list.astype('uint8'), 'RGB')
        #PIL_image.save('test.jpg')
        px_list = numpy.array(px_list,dtype='uint8')
        px_list = numpy.reshape(px_list,self.image_shape)

        
        print(px_list)
       
        #px_list = numpy.uint8(px_list)
        self.view_image(px_list)
        
        #self.view_image(image)
        #return image
    
    def uncorrupt_image_api(self,cor_image,hash1,hash2):
        key = self.create_key(hash2,hash1)
        #new edit
        x_key = max(hash1) * min(hash1)
        key_len = len(key)
        index_of_key = 0
        px_list = []
        for x in cor_image:
            if index_of_key == key_len:
                index_of_key = 0
            
            key_value = key[index_of_key]
            px_list.append((int(x) - key_value)-x_key)
            index_of_key +=1

        return px_list
    
    def decrypt_api(self,cor_image):
        selected_fp = str(input('Select FP | [P1 , P2] -> '))
        raw_fp = ''
        raw_fp_sha1 = ''
        raw_fp_sha256 = ''
        if selected_fp == 'P1' or selected_fp == 'p1':
            raw_fp = self.finger_templates['Heba']
            selected_fp = raw_fp
            print('Heba Fingerprint Template Loaded To Working Varible')
        elif selected_fp == 'P2' or selected_fp == 'p2':
            raw_fp = self.finger_templates['Salma']
            selected_fp = raw_fp
            print('Heba Fingerprint Template Loaded To Working Varible')
        else:
            self.protect_image()
        
        
        raw_fp_sha1 = self.sha1_hash(raw_fp)
        raw_fp_sha256 = self.sha256_hash(raw_fp)
        
        encoded_hash_sha1 = self.hash_to_ascii(raw_fp_sha1)
        encoded_hash_sha256 = self.hash_to_ascii(raw_fp_sha256)
        uncorrupted_image = self.uncorrupt_image_api(cor_image,encoded_hash_sha1,encoded_hash_sha256)
        return uncorrupted_image

    
    def protect_image(self):
        selected_fp = str(input('Select FP | [P1 , P2] -> '))
        raw_fp = ''
        raw_fp_sha1 = ''
        raw_fp_sha256 = ''
        if selected_fp == 'P1' or selected_fp == 'p1':
            raw_fp = self.finger_templates['Heba']
            selected_fp = raw_fp
            print('Heba Fingerprint Template Loaded To Working Varible')
        elif selected_fp == 'P2' or selected_fp == 'p2':
            raw_fp = self.finger_templates['Salma']
            selected_fp = raw_fp
            print('Heba Fingerprint Template Loaded To Working Varible')
        else:
            self.protect_image()
        
        
        raw_fp_sha1 = self.sha1_hash(raw_fp)
        raw_fp_sha256 = self.sha256_hash(raw_fp)
        print('Template : ',raw_fp)
        print('Bio Sha1 : ',raw_fp_sha1)
        print('Bio Sha256 : ',raw_fp_sha256)
        #encoded_hash_sha1 = self.hash_to_ascii_pixels(raw_fp_sha1)
        #encoded_hash_sha256 = self.hash_to_ascii_pixels(raw_fp_sha256)
        encoded_hash_sha1 = self.hash_to_ascii(raw_fp_sha1)
        encoded_hash_sha256 = self.hash_to_ascii(raw_fp_sha256)
        corrupted_image = self.corrupt_image(self.working_image,encoded_hash_sha1,encoded_hash_sha256)
        self.export_bpi(corrupted_image,raw_fp_sha256)
        #edit 
        ##corrupted_image = self.read_bpi()
        ##uncorrupted_image = self.uncorrupt_image(corrupted_image,encoded_hash_sha1,encoded_hash_sha256)
        #self.export_file(self.working_image,raw_fp_sha256)
        

        







