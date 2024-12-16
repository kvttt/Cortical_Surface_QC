import os
from pypdf import PdfWriter
import glob
from create_pdf import plot_all
from tqdm import tqdm
from datetime import datetime
import time
import sys


def txt_to_list(file_path):
    sub_lst = []
    ses_lst = []
    with open(file_path, 'r') as f:
        for line in f:
            sub_lst.append(line.strip().split('/')[-2])
            ses_lst.append(line.strip().split('/')[-1])
    return sub_lst, ses_lst


def get_pdf_metadata():
    # Format the current date and time for the metadata
    utc_time = "-05'00'"  # UTC time optional
    time = datetime.now().strftime(f"D\072%Y%m%d%H%M%S{utc_time}")

    # Add the new metadata
    meta = {
        "/Author": "Kaibo Tang",
        "/Producer": "pypdf 5.1.0",
        "/CreationDate": time,
        "/ModDate": time,
        "/Creator": __file__,
    }
    return meta


def merge_pdf(output_path, group_num):
    pdf_lst = glob.glob(os.path.join(output_path, '*.pdf'))
    pdf_lst.sort()
    merger = PdfWriter()
    meta = get_pdf_metadata()
    merger.add_metadata(meta)
    for pdf in pdf_lst:
        merger.append(pdf)
    merger.write(os.path.join(output_path, f'group_{group_num}.pdf'))
    merger.close()


def create_csv(output_path, ct5_lst, ct95_lst, cv5_lst, cv95_lst, group_num):
    pdf_lst = glob.glob(os.path.join(output_path, '*.pdf'))
    res = pdf_lst
    pdf_lst.sort()
    pdf_lst = pdf_lst[:50]
    pdf_lst = [
        pdf.split('/')[-1].split('.')[0] for pdf in pdf_lst
    ]
    index_lst = [
        pdf.split('_')[0] for pdf in pdf_lst
    ]
    sub_lst = [
        '_'.join(pdf.split('_')[1:4]) for pdf in pdf_lst
    ]
    ses_lst = [
        pdf.split('_')[4] for pdf in pdf_lst
    ]
    with open(os.path.join(output_path, f'group_{group_num}.csv'), 'w') as f:
        f.write('Index,Subject,Session,Thickness@5,Thickness@95,Curvature@5,Curvature@95,Score\n')
        for index, sub, ses, ct5, ct95, cv5, cv95 in zip(index_lst, sub_lst, ses_lst, ct5_lst, ct95_lst, cv5_lst, cv95_lst):
            f.write(f'{index},{sub},{ses},{ct5},{ct95},{cv5},{cv95},\n')
    return res


def create_pdf_all(output_path, sub_lst, ses_lst, group_num):
    ct5_lst, ct95_lst, cv5_lst, cv95_lst = [], [], [], []
    for index, sub, ses in tqdm(zip(range(len(sub_lst)), sub_lst, ses_lst)):
        file_path = os.path.join('/home/kaibo/DATA', sub, ses)
        fn, ct5, ct95, cv5, cv95 = plot_all(file_path, output_path, index, group_num)
        ct5_lst.append(ct5)
        ct95_lst.append(ct95)
        cv5_lst.append(cv5)
        cv95_lst.append(cv95)
        # print(fn)
    return ct5_lst, ct95_lst, cv5_lst, cv95_lst


def prepare_all(output_path, group_num):
    output_folder = os.path.join(output_path, f'group_{group_num}')
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    sub_lst, ses_lst = txt_to_list(f'./group/group_{group_num}.txt')
    ct5_lst, ct95_lst, cv5_lst, cv95_lst = create_pdf_all(output_folder, sub_lst, ses_lst, group_num)
    merge_pdf(output_folder, group_num)
    pdf_lst = create_csv(output_folder, ct5_lst, ct95_lst, cv5_lst, cv95_lst, group_num)
    for pdf in pdf_lst[:50]:
        os.remove(pdf)
    print(f'Group {group_num:03d} saved to {output_folder}')


if __name__ == "__main__":
    group_num = int(sys.argv[1])
    print('=' * 15, f'Group {group_num:03d}', '=' * 15)
    t0 = time.time()
    prepare_all('./', group_num)
    print(f'Time elapsed: {time.time() - t0:.2f} s')
