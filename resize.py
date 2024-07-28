from PIL import Image
import os



def resize_images(input_folder, output_folder, scale_factor):
    
    
    
    # フォルダ内の画像を処理
    for filename in os.listdir(input_folder):
        if filename.endswith(".jpg") or filename.endwith(".png"):
            
            # 画像を開く
            img_path = os.path.join(input_folder, filename)
            img = Image.open(img_path)
                
            # 画像の幅と高さをスケールファクターに基づいて変更
            new_width = int(img.width * scale_factor)
            new_height = int(img.height * scale_factor)
                
            # 画像を新しいサイズにリサイズする処理
            resized_img = img.resize((new_width, new_height), Image.ANTIALIAS)
                
            # 出力フォルダにリサイズされた画像を保存
            output_path = os.path.join(output_folder, filename)
            resized_img.save(output_path)



dir_list = ["jacket","pants","shirt","skirt","t-shirt","underwear",]


for i in range(len(dir_list)):
    input_folder_path = f"./static/images/clothes/{dir_list[i]}" # 元画像があるパス
    output_folder_path = f"./static/images/clothes/in_{dir_list[i]}" # リサイズされた画像を保存をするフォルダのパス
    scaling_factor = 4 # サイズを2倍にする
                
    resize_images(input_folder_path, output_folder_path, scaling_factor)
            

