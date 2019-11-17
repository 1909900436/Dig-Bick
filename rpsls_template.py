# coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ�����
���ڣ�2019.11.14
"""

import random


# 0 - ʯͷ
# 1 - ʷ����
# 2 - ֽ
# 3 - ����
# 4 - ����

# ����Ϊ�����Ϸ����Ҫ�õ����Զ��庯��

def name_to_number(name):
    """
    ����Ϸ�����Ӧ����ͬ������
    """

    # ʹ��if/elif/else��佫����Ϸ�����Ӧ����ͬ������
    # ��Ҫ���Ƿ��ؽ��

    if name == 'ʯͷ':
        return 0
    elif name == 'ʷ����':
        return 1
    elif name == 'ֽ':
        return 2
    elif name == '����':
        return 3
    elif name == '����':
        return 4
    else:
        print('Error: No Correct Name')

def number_to_name(number):
    """
    ������ (0, 1, 2, 3, or 4)��Ӧ����Ϸ�Ĳ�ͬ����
    """

    # ʹ��if/elif/else��佫��ͬ��������Ӧ����Ϸ�Ĳ�ͬ����
    # ��Ҫ���Ƿ��ؽ��

    if number == 0:
        return 'ʯͷ'
    elif number == 1:
        return 'ʷ����'
    elif number == 2:
        return 'ֽ'
    elif number == 3:
        return '����'
    elif number == 4:
        return '����'


def rpsls(choice_name):
	"""
	�û�����������һ��ѡ�񣬸���RPSLS��Ϸ��������Ļ�������Ӧ�Ľ��
	"""

	print('----------------')
    # ���"-------- "���зָ�

	print('����ѡ��Ϊ��', choice_name)
	player_choice = choice_name
    # ��ʾ�û�������ʾ���û�ͨ�����̽��Լ�����Ϸѡ��������룬�������player_choice

	player_choice_number = name_to_number(player_choice)
    # ����name_to_number()�������û�����Ϸѡ�����ת��Ϊ��Ӧ���������������player_choice_number

	comp_number = random.randrange(0, 5)
    # ����random.randrange()�Զ�����0-4֮��������������Ϊ��������ѡ�����Ϸ���󣬴������comp_number

	comp_choice = number_to_name(comp_number)
    # ����number_to_name()����������������������ת��Ϊ��Ӧ����Ϸ����

	print('�������ѡ��Ϊ��', comp_choice)
    # ����Ļ����ʾ�����ѡ����������

	dif = player_choice_number - comp_number
	if dif == 1 or dif==2 or dif==-3 or dif==-4:
		print('��Ӯ�ˣ�')
	elif dif == 0:
		print('���ͻ�������һ���أ�')
	elif dif == -1 or dif==-2 or dif==3 or dif==4:
		print('����Ӯ�ˣ�')


# ����if/elif/else ��䣬����RPSLS������û�ѡ��ͼ����ѡ������жϣ�������Ļ����ʾ�жϽ��
# ����û��ͼ����ѡ��һ��������ʾ�����ͼ��������һ���ء�������û���ʤ������ʾ����Ӯ�ˡ�����֮����ʾ�������Ӯ�ˡ�


# �Գ�����в���
print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
choice_name = input('����������ѡ��')
rpsls(choice_name)
