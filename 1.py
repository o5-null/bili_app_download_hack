import json
from pathlib import Path
import tqdm
def read_json(json_path):
     with open(str(json_path),'rb') as f:
    #定义为只读模型，并定义名称为f
        params = json.load(f)
        return params
    
def write_json(json_path,data):
    with open(json_path,'w') as f:
        json.dump(data,f)

print('遍历文件夹')
all_dir = Path.cwd().iterdir()
for one in all_dir:
    if one.is_dir():
        for one_one in one.iterdir():
            if one_one.is_dir() and Path(one_one / 'entry.json').exists():
                old_data = read_json(Path(one_one / 'entry.json').resolve())
                print('检查'+old_data['title'])
                if old_data['video_quality'] > 80:
                    old_sav_data = read_json(one_one / str(old_data['video_quality']) / 'index.json')
                    new_sav_data = {}
                    for sav_one in old_sav_data['video']:
                        sav_one['id'] = 80
                        new_sav_data['video'] =[]
                        new_sav_data['video'].append(sav_one)
                    new_sav_data['audio'] = old_sav_data['audio']
                    write_json(one_one / str(old_data['video_quality']) / 'index.json',new_sav_data)
                    print('缓存文件修改完成')

                    Path(one_one / str(old_data['video_quality'])).rename(one_one / '80')
                    print('缓存文件修改名字完成')
                    
                    new_data = old_data
                    print('该缓存为大会员，hack中')
                    new_data['type_tag'] = '80'
                    new_data['video_quality'] = 80
                    new_data['prefered_video_quality'] = 80
                    write_json(Path(one_one / 'entry.json'),old_data)
                    print(old_data['title']+' '+str(old_data['avid'])+' 核心文件处理完毕')

