import os
from pathlib import Path
import config
import xmlschema
from xml.etree import ElementTree
import paramiko


hostname = "gadi.nci.org.au"
username = "mk4729"


ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect(hostname, username=username, password="klimenkoM_379")
sftp = ssh.open_sftp()

# with sftp.open("/scratch/hh39/mk4729/graphene_ab_bilayer_rect/tmp_ab_bilayer_scf/ab_bilayer_scf.xml", "r") as f:
with sftp.open("/scratch/hh39/mk4729/graphene_ab_bilayer_rect/pp.in", "r") as f:
    text = f.read()

sftp.get("/scratch/hh39/mk4729/graphene_ab_bilayer_rect/tmp_ab_bilayer_scf/ab_bilayer_scf.xml",
         "/Users/mkly0001/Monash_work/nci_results/ab_bilayer_scf.xml")
sftp.close()
ssh.close()


def xml2dict(path):

    base_dir = Path(__file__).resolve().parent
    config_path = base_dir / "config.cfg"
    cfg = config.Config(str(config_path))

    data = ElementTree.parse(path).getroot()
    qes = data.items()[0][1].split()[1].split('/')[-1].split('.')[0]
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, cfg[qes])
    schema = xmlschema.XMLSchema(file_path)
    data_dict = schema.to_dict(data)

    return data_dict


if __name__=='__main__':

    path='/Users/mkly0001/Monash_work/nci_results/ab_bilayer_scf.xml'

    a = xml2dict(path)
    print(a['output']['basis_set']['fft_grid'].values())