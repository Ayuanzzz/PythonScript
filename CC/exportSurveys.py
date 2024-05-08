import os
import sys

import ccmasterkernel

base_path = r"\\172.16.0.16\data70\xizang"
folder_names = [f for f in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, f))]
err_list = []
pro_list=[]
exist_list = ['zhubasi', 'rongtangsi', 'xianlasi', 'bairihajiasi', 'baidazequlakangsi', 'waleduobinglakang', 'gonglongsi', 'qiemorizhui', 'narizhui', 'quyamarizhui', 'larisi', 'qingzhensi', 'xiapusi', 'qiongcangsi', 'longlasi','longlasi', 'longlasi', 'duokarizhui', 'dahaisi', 'langlayongzhongdangzhalin', 'baidengsi', 'morongsi', 'gamurizhui', 'tangzasi', 'rendarizhui', 'zongguorizhui', 'shajiasi', 'weisesi', 'enairizhui', 'chayisi(tmp)', 'pozhangsi', 'sedengsi', 'yachurizhui', 'xumusi', 'bagasi', 'shalongrizhui', 'guozisi', 'wutangsi', 'waqingrizhui', 'zhangkasi', 'angsuosi', 'banlaiteqiuqukelinsi', 'zizhusi', 'eduosi', 'zhuomarizhui', 'qugasangdinglin', 'daresi', 'xiangkangsi', 'jiangcuolinsi', 'ziqingrizhui', 'xucangsi', 'guduorizhui', 'kahongsi', 'jiasangkasi', 'gangpurizhui', 'gedangsi', 'jisesi', 'dongchongsi', 'leransi', 'rongmaigensasi', 'qiangbalinsi', 'zongluosi', 'yuezisi', 'wutongsi', 'siderizhui', 'jiangjiangsi', 'baxiongsi', 'renqinglinsi', 'kangmasi', 'jinkasi', 'shayisi', 'zaranrizhui', 'naiduosi', 'jisangsi', 'shuodusi', 'kecharizhui', 'zongluobulinsi', 'dangzesi', 'xialangmudingsi', 'jiaguosi', 'guojinranselakang', 'bengnangsi', 'xiangdengsi', 'yuedasi', 'gangmeirizhui', 'luobulinsi', 'sajiasi(废弃)', 'kangbasi','galaisi', 'lunzhusiZGX', 'shalasi', 'chabengsi', 'jiaransangpeiluobulin', 'qiangzongsi', 'subusi', 'zuozisi', 'gurulongrizhui', 'nuozhasi', 'ladingsi', 'qiongzongrizhui', 'gongqiulakang', 'zhaduisi', 'lingdasi', 'tukasi', 'gentangsi', 'diguosi', 'dedingsi', 'yuririzhui', 'pulongsi', 'pulongsi', 'rinaisi', 'sharaosi', 'banggasi', 'badangsi', 'gawalongsi', 'bengyasi', 'dangqiasi', 'deqinlunzhusi', 'wangkalakang', 'lazisi', 'migerichugedengsangpeilin', 'zhengarizhui', 'baiguosi', 'duodongsi', 'duodongsi', 'duodasi', 'gangdasi', 'zhapeisi', 'dagasi', 'hezongsi', 'dajiangrizhui', 'puraorizhui', 'xiasangsi', 'jirisimangkang', 'xiachikarizhui', 'bameisi', 'guolongsi', 'seduosi', 'shadongrizhui', 'yibasi', 'jirisikanuo', 'sesuorizhui', 'bajuerizhui', 'xiaousi', 'dijiangrizhui', 'dangpuzengdengsi', 'xiagaojisi', 'lawasi', 'nuozhasifensi', 'baresi', 'gangmeirizhuiLWQ', 'wuyasi', 'zizhurizhui', 'gegekexiusi', 'benzhonglakang', 'chaduosi', 'dazhuosasi', 'zhuomarizhuiLLX', 'zhigasi', 'gongguosi', 'guoguosi', 'cuokarizhui', 'shanggaojisi', 'baxiarizhui', 'banggangsi', 'zhaguosi', 'gapusi', 'jianggusi', 'gandansi', 'bianbasi', 'gamasi', 'riguosi', 'naitangsi', 'yadasi', 'kebalongsi', 'yurensi', 'xiasemazongsi', 'reherizhui', 'weichengsi', 'rongbusi', 'wanggegongsongsangdenglin', 'zhubasimangkang']

def exportSurvey(projectFile, projectDirPath, folderName):
    print(projectDirPath)
    # load project
    project = ccmasterkernel.Project()
    err = project.readFromFile(projectFile)
    if not err.isNone():
        print(err.message)
        err_list.append(folder_name)
    print('Project %s started.' % project.getName())
    # get block
    block_num = project.getNumBlocks()
    if not block_num:
        return
    block = project.getBlock(block_num - 1)
    recNum = block.getNumReconstructions()
    if recNum:
        rec = block.getReconstruction(0)
        srs = rec.getSRS()
        surveyDataExportOptions = ccmasterkernel.SurveyDataExportOptions()
        surveyDataExportOptions.includeUTP = False
        surveyDataExportOptions.includeCP = True
        surveyDataExportOptions.srs = srs
        surveyName = folderName + "cp" + ".xml"
        block.exportSurveyData(os.path.join(projectDirPath, surveyName), surveyDataExportOptions)
    else:
        print("no rec")


for folder_name in folder_names:
    print(folder_name)
    if folder_name not in exist_list:
        folder_path = os.path.join(base_path, folder_name)
        for dirpath, dirnames, filenames in os.walk(folder_path):
            for filename in filenames:
                if filename.endswith(".ccm") and "副本" not in filename:
                    ccm_file_path = os.path.join(dirpath, filename)
                    print(ccm_file_path)
                    pro_list.append(folder_name)
                    print(pro_list)
                    exportSurvey(ccm_file_path, folder_path, folder_name)

print(err_list)
print("done")
