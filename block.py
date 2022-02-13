import json
import os
import hashlib

blockchain_dir = 'block/'

def get_hash(prev_block):
    with open(blockchain_dir + prev_block, 'rb') as f:
        content = f.read()
    return hashlib.sha256(content).hexdigest()

def check_integrity():
        files = sorted(os.listdir(blockchain_dir), key=lambda x: int(x))

        results = []
        
        for file in files[1:]:
            with open(blockchain_dir + file) as f:
                block = json.load(f)

            prev_hash = block.get('prev_block').get('hash')
            prev_filename = block.get('prev_block').get('filename')

            actual_hash = get_hash(prev_filename)

            if prev_hash == actual_hash:
                res = 'OK'
            else:
                res = 'Was Changed'

            print(f'Block {prev_filename}: {res}')
            results.append({'block': prev_filename, 'result': res})
        return results

def write_block(map, team_win, team_lost, win_score, lost_score, mvp):

    block_count = len(os.listdir(blockchain_dir))
    prev_block = str(block_count-1)
    current_block = str(len(os.listdir(blockchain_dir)))
    current_block_path = blockchain_dir + current_block

    data = {
        "block_index": current_block,
        "map": map,
        "team_win": team_win,
        "team_lost": team_lost,
        "win_score": win_score,
        "lost_score": lost_score,
        "mvp": mvp,
        "prev_block": {
            "hash": get_hash(prev_block),
            "filename": prev_block
        }
    }

    with open(current_block_path, 'w') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
        f.write('\n')

def view_block(block_view):
    with open(blockchain_dir + block_view, 'r') as f:
        block = json.load(f)
        content = []
        content.append("Map: " + block.get('map'))
        content.append("Team Win: " + block.get('team_win'))
        content.append("Team Lost: " + block.get('team_lost'))
        content.append("Team Win Score: " + block.get('win_score'))
        content.append("Team Lost Score: " + block.get('lost_score'))
        content.append("Match MVP: " + block.get('mvp'))
        print(*content, sep = "\n")

def main():
    print("Wellcome to Valorant Database")
    run = True
    while(run):
        print("Select Mode")
        print("1: Add Match Information")
        print("2: View match Information")
        print("3: Check Integrity")
        print("0: Exit")
        mode = int(input("Your Select: "))
        print()

        if(mode == 1):
            map = input("Enter Map: ")
            team_win = input("Enter Team Win: ")
            team_lost = input("Enter Team Lost: ")
            win_score = input("Enter Team Win Score: ")
            lost_score = input("Enter Team Lost Score: ")
            mvp = input("Match MVP: ")
            write_block(map, team_win, team_lost, win_score, lost_score, mvp)
            print()
        elif(mode == 2):
            num = input("Enter Number of Block: ")
            print()
            view_block(num)
            print()
        elif(mode == 3):
            print()
            check_integrity()
            print()
        elif(mode == 0):
            run = False
        else:
            print("Wrong Input!!!")
            print()



if __name__=='__main__':
    main()