import os, math, sys, importlib
importlib.reload(sys)
from flask import Flask, render_template, request, send_from_directory, redirect, url_for

app = Flask(__name__)

@app.route('/')
def front():
    return render_template('front.html')

@app.route('/index', methods=['POST'])
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    
    objects = {}
    # function to add values to dictionary 
    def add_objects(serial_number, object_name, process_area, complexity, etlr_selected, threshold_volume, extra_data_volume, dq_selected):
        objects.update({
            serial_number:{
                'Object Name': object_name,
                'Process Area': process_area, 
                'Complexity':complexity, 
                'ETLR Selected': etlr_selected,
                'DQ Selected': dq_selected,
                'Threshold Volume': threshold_volume,
                'Extra Data Volume':extra_data_volume
                }
            })

    selected_objects = {}
    def add_selected_objects(name, serial_number, object_name, process_area, complexity, threshold_volume):
        name.update({
            serial_number:{
                'Object Name': object_name,
                'Process Area': process_area, 
                'Complexity':complexity, 
                'Threshold Volume': threshold_volume
                }
            })
        return

    # created objects
    add_objects(1, 'House Bank', 'FI', 'Very Low', 0, 45000, 0, 0)
    add_objects(2, 'CO Config', 'FI', 'Very Low', 0, 20000, 0, 0)
    add_objects(3, 'G/L Accounts', 'FI', 'Very Low', 0, 35000, 0, 0)
    add_objects(4, 'Profit Center (Profit center group)', 'FI', 'Low', 0, 20000, 0, 0)
    add_objects(5, 'Cost Center (Cost center group)', 'FI', 'Low', 0, 18000, 0, 0)
    add_objects(6, 'Tax Keys', 'FI', 'Low', 0, 40000, 0, 0)
    add_objects(7, 'Bank Key(customer, supplier)', 'FI', 'Low', 0, 28000, 0, 0)
    add_objects(8, 'Customer', 'SD', 'Very High', 0, 500000, 0, 0)
    add_objects(9, 'Supplier', 'P2P', 'Very High', 0, 450000, 0, 0)
    add_objects(10, 'Products', 'PP', 'Very High', 0, 400000, 0, 0)
    add_objects(11, 'Credit Management', 'FI', 'Medium', 0, 150000, 0, 0)
    add_objects(12, 'Characteristics', 'PP', 'Low', 0, 600000, 0, 0)
    add_objects(13, 'Class', 'PP', 'Low', 0, 550000, 0, 0)
    add_objects(14, 'Commodity Codes-Creation', 'P2P', 'Low', 0, 5000, 0, 0)
    add_objects(15, 'Product Classification', 'P2P', 'Low', 0, 8000, 0, 0)
    add_objects(16, 'Work Center', 'PP', 'Medium', 0, 120000, 0, 0)
    add_objects(17, 'Purchase Contract', 'P2P', 'High', 0, 80000, 0, 0)
    add_objects(18, 'Source List', 'P2P', 'Medium', 0, 30000, 0, 0)
    add_objects(19, 'Catalog code group/code', 'QM', 'Medium', 0, 50000, 0, 0)
    add_objects(20, 'Selected set', 'QM', 'Medium', 0, 60000, 0, 0)
    add_objects(21, 'Selected set code', 'QM', 'Medium', 0, 40000, 0, 0)
    add_objects(22, 'Inspection Method', 'QM', 'Medium', 0, 50000, 0, 0)
    add_objects(23, 'Sampling Procedures', 'QM', 'Medium', 0, 45000, 0, 0)
    add_objects(24, 'Master Recipe', 'QM', 'Very High', 0, 250000, 0, 0)
    add_objects(25, 'Material BOM', 'PP', 'High', 0, 200000, 0, 0)
    add_objects(26, 'Material Batch Classification', 'PP', 'Medium', 0, 120000, 0, 0)
    add_objects(27, 'Batch Unique at mat and client level', 'PP', 'High', 0, 80000, 0, 0)
    add_objects(28, 'Inspection Characteristic', 'QM', 'Medium', 0, 40000, 0, 0)
    add_objects(29, 'Dynamic Modification Rule', 'QM', 'Medium', 0, 70000, 0, 0)
    add_objects(30, 'Inspection Plan', 'QM', 'Medium', 0, 80000, 0, 0)
    add_objects(31, 'Quality View Extention', 'QM', 'Low', 0, 65000, 0, 0)
    add_objects(32, 'Material Inspection Setup', 'QM', 'Low', 0, 90000, 0, 0)
    add_objects(33, 'Routings', 'PP', 'Medium', 0, 180000, 0, 0)
    add_objects(34, 'Production Versions', 'PP', 'Medium', 0, 170000, 0, 0)
    add_objects(35, 'Purchasing info records', 'P2P', 'High', 0, 220000, 0, 0)
    add_objects(36, 'Certificate profile creation', 'QM', 'Medium', 0, 320000, 0, 0)
    add_objects(37, 'Certificate profile assignment', 'QM', 'Medium', 0, 430000, 0, 0)
    add_objects(38, 'Output Condition Record', 'QM', 'Medium', 0, 270000, 0, 0)
    add_objects(39, 'Condition record for pricing (general template)', 'SD', 'Medium', 0, 460000, 0, 0)
    add_objects(40, 'Maintenance Workcenter', 'PM', 'Medium', 0, 120000, 0, 0)
    add_objects(41, 'Functional Location', 'PM', 'High', 0, 600000, 0, 0)
    add_objects(42, 'Equipment', 'PM', 'Very High', 0, 680000, 0, 0)
    add_objects(43, 'General maintenance task list', 'PM', 'Medium', 0, 340000, 0, 0)
    add_objects(44, 'Maintenance Plan', 'PM', 'Medium', 0, 280000, 0, 0)
    add_objects(45, 'Maintenance Item', 'PM', 'Medium', 0, 450000, 0, 0)
    add_objects(46, 'Customer Material', 'SD', 'Medium', 0, 340000, 0, 0)
    add_objects(47, 'EWM Warehouse Bin Template', 'MM', 'High', 0, 320000, 0, 0)
    add_objects(48, 'EWM Product Master', 'MM', 'High', 0, 230000, 0, 0)
    add_objects(49, 'EWM Packaging Material', 'MM', 'High', 0, 180000, 0, 0)
    add_objects(50, 'EWM Inbound Pack Spec', 'MM', 'High', 0, 270000, 0, 0)
    add_objects(51, 'EWM PSA Control Cycle', 'MM', 'Medium', 0, 320000, 0, 0)
    add_objects(52, 'Fixed assets incl. Balances & transactions', 'FI', 'Very High', 0, 350000, 0, 0)
    add_objects(53, 'Bank account balance', 'FI', 'High', 0, 170000, 0, 0)
    add_objects(54, 'Accounts payable open item', 'FI', 'High', 0, 240000, 0, 0)
    add_objects(55, 'Accounts receivable open item', 'FI', 'High', 0, 240000, 0, 0)
    add_objects(56, 'G/L Acc balance & open/line item', 'FI', 'High', 0, 250000, 0, 0)
    add_objects(57, 'Sales order (only open SO)', 'SD', 'High', 0, 320000, 0, 0)
    add_objects(58, 'Purchase order (only open PO)', 'P2P', 'High', 0, 380000, 0, 0)
    add_objects(59, 'Inventory Balance (IM Inventory)', 'MM', 'Very High', 0, 200000, 0, 0)
    add_objects(60, 'EWM Warehouse Inventory', 'MM', 'Medium', 0, 180000, 0, 0)
    add_objects(61, 'Project Definition', 'PS', 'Medium', 0, 190000, 0, 0)
    add_objects(62, 'WBS elements', 'PS', 'Medium', 0, 280000, 0, 0)
    add_objects(63, 'Real Estate Contract', 'ReFX', 'Low', 0, 380000, 0, 0)
    add_objects(64, 'Building', 'ReFX', 'Low', 0, 0, 0, 0)
    add_objects(65, 'Land', 'ReFX', 'Low', 0, 0, 0, 0)
    add_objects(66, 'Rental Object', 'ReFX', 'Low', 0, 0, 0, 0)
    add_objects(67, 'Business Entity', 'ReFX', 'Low', 0, 0, 0, 0)
    add_objects(68, 'Architectural object', 'ReFX', 'Low', 0, 0, 0, 0)
    add_objects(69, 'Merchandise category hierarchy', 'IS-Retail', 'Very Low', 0, 0, 0, 0)
    add_objects(70, 'Article/Product Hierarchy', 'IS-Retail', 'Very Low', 0, 0, 0, 0)
    add_objects(71, 'Site Master (Store/DC/Warranty/WH/HQ)', 'IS-Retail', 'Very Low', 0, 0, 0, 0)
    add_objects(72, 'Merchandise category', 'IS-Retail', 'Very Low', 0, 0, 0, 0)
    add_objects(73, 'Site grouping', 'IS-Retail', 'Very Low', 0, 0, 0, 0)
    add_objects(74, 'Business Partner (Customer Master data (Loyalty, E-Com) - Retail)', 'IS-Retail', 'Very Low', 0, 0, 0, 0)
    add_objects(75, 'Item master/Product Master/Article master', 'IS-Retail', 'Very Low', 0, 0, 0, 0)
    add_objects(76, 'Retail Pricing', 'IS-Retail', 'Very Low', 0, 0, 0, 0)
    add_objects(77, 'Retail Promotions & Markdowns', 'IS-Retail', 'Very Low', 0, 0, 0, 0)
    add_objects(78, 'Assortment', 'IS-Retail', 'Very Low', 0, 0, 0, 0)
    add_objects(79, 'Suppliers Rebate & Contracts', 'IS-Retail', 'Very Low', 0, 0, 0, 0)
    add_objects(80, 'Open Inventory', 'IS-Retail', 'Very Low', 0, 0, 0, 0)
    add_objects(81, 'Open Stock transfer Order', 'IS-Retail', 'Very Low', 0, 0, 0, 0)
    add_objects(82, 'Open Purchase Orders in (Trade)', 'IS-Retail', 'Very Low', 0, 0, 0, 0)
    add_objects(83, 'Statistical Key figure', 'CO', 'Very Low', 0, 60000, 0, 0)
    add_objects(84, 'Internal order', 'CO', 'Very Low', 0, 250000, 0, 0)
    add_objects(85, 'Activity type', 'FI', 'Very Low', 0, 80000, 0, 0)
    add_objects(86, 'Client segmentation - Credit (2 templates)', 'FI', 'Very Low', 0, 80000, 0, 0)
    add_objects(87, 'Employee', 'HCM', 'Very Low', 0, 320000, 0, 0)
    add_objects(88, 'Commodity codes material assignment', 'MM', 'Very Low', 0, 120000, 0, 0)
    add_objects(89, 'Object classification', 'MM', 'Very Low', 0, 160000, 0, 0)
    add_objects(90, 'Material Variant', 'MM', 'Very Low', 0, 140000, 0, 0)
    add_objects(91, 'Material long text', 'PP', 'Very Low', 0, 500000, 0, 0)
    add_objects(92, 'Open production order', 'PP', 'Very Low', 0, 240000, 0, 0)
    add_objects(93, 'PIR(Planned Independent Requirement) for forecast', 'PP', 'Very Low', 0, 190000, 0, 0)
    add_objects(94, 'Setup group assignment(routing)', 'PP', 'Very Low', 0, 180000, 0, 0)
    add_objects(95, 'Quality info record', 'QM', 'Very Low', 0, 140000, 0, 0)
    add_objects(96, 'Email determination in Sales', 'SD', 'Very Low', 0, 130000, 0, 0)
    add_objects(97, 'Sales contracts (open items)', 'SD', 'Very Low', 0, 300000, 0, 0)
    add_objects(98, 'Location', 'TM', 'Very Low', 0, 280000, 0, 0)
    add_objects(99, 'Charge type', 'TM', 'Very Low', 0, 40000, 0, 0)
    add_objects(100, 'Freight agreement', 'TM', 'Very Low', 0, 60000, 0, 0)
    add_objects(101, 'Transportation zone', 'TM', 'Very Low', 0, 80000, 0, 0)

    def taking_input(objects):
        choices_list = (request.form.getlist(objects))
        chosen_objects = [eval(i) for i in choices_list]
        return chosen_objects

    etlr_chosen_objects = taking_input('objects')
    dq_chosen_objects = taking_input('dq_objects')
    dv_chosen_objects = taking_input('dv_objects')

    etlr_selected_objects = {}
    dq_selected_objects = {}
    dv_selected_objects = {}


    # updating the selected variable as per the user choices 
    for i in range(0, len(etlr_chosen_objects)):
        objects[etlr_chosen_objects[i]]['ETLR Selected'] = 1

    for i in range(0, len(dq_chosen_objects)):
        objects[dq_chosen_objects[i]]['DQ Selected'] = 1

    for i in range(0, len(dv_chosen_objects)):
        if objects[etlr_chosen_objects[i]]['ETLR Selected'] == 1:
            objects[dv_chosen_objects[i]]['Extra Data Volume'] = 1
        else:
            continue 

    # iterating over objects dictionary
    def creating_selected_obj_dict(selected, selected_objects):
        for outer_key, outer_value in objects.items():
            # checking if the selected key is 1
            if objects[outer_key][selected] == 1:
                if selected not in selected_objects:
                    add_selected_objects(selected_objects, outer_key, objects[outer_key]['Object Name'], objects[outer_key]['Process Area'], objects[outer_key]['Complexity'], objects[outer_key]['Threshold Volume'])

    etlr_selected_objects = creating_selected_obj_dict('ETLR Selected', etlr_selected_objects)
    dq_selected_objects = creating_selected_obj_dict('DQ Selected', dq_selected_objects)
    dv_selected_objects = creating_selected_obj_dict('Extra Data Volume', dv_selected_objects)

    # counting different types of objects 
    def counting_number_of_objects(selected):
        number_of_vlow_objects = 0
        number_of_low_objects = 0
        number_of_medium_objects = 0
        number_of_high_objects = 0
        number_of_vhigh_objects = 0
        for i in objects:
            if objects[i][selected] == 1:
                if objects[i]['Complexity'] == 'Very Low':
                    number_of_vlow_objects = number_of_vlow_objects + 1
                elif objects[i]['Complexity'] == 'Low':
                    number_of_low_objects = number_of_low_objects + 1
                elif objects[i]['Complexity'] == 'Medium':
                    number_of_medium_objects = number_of_medium_objects + 1
                elif objects[i]['Complexity'] == 'High':
                    number_of_high_objects = number_of_high_objects + 1
                else:
                    number_of_vhigh_objects = number_of_vhigh_objects + 1
            else:
                continue
        
        total_objects = number_of_high_objects + number_of_low_objects + number_of_medium_objects + number_of_vhigh_objects + number_of_vlow_objects

        return number_of_vlow_objects, number_of_low_objects, number_of_medium_objects, number_of_high_objects, number_of_vhigh_objects, total_objects

    etlr_number_of_vlow_objects, etlr_number_of_low_objects, etlr_number_of_medium_objects, etlr_number_of_high_objects, etlr_number_of_vhigh_objects, etlr_total_objects = counting_number_of_objects('ETLR Selected')

    dq_number_of_vlow_objects, dq_number_of_low_objects, dq_number_of_medium_objects, dq_number_of_high_objects, dq_number_of_vhigh_objects, dq_total_objects  = counting_number_of_objects('DQ Selected')

    dv_number_of_vlow_objects, dv_number_of_low_objects, dv_number_of_medium_objects, dv_number_of_high_objects, dv_number_of_vhigh_objects, dv_total_objects = counting_number_of_objects('Extra Data Volume')

    def calculate_hours_per_complexity (etlr_number_of_objects, number_of_days_bods, number_of_days_bods_recon, number_of_days_dl, extra_data_volume, extra_threshold_hours, dq_number_of_objects, number_of_days_dq):
        total_build_hours_bods = (etlr_number_of_objects*9*number_of_days_bods)+(extra_data_volume*extra_threshold_hours)
        total_build_hours_bods_recon = (etlr_number_of_objects*9*number_of_days_bods_recon)
        number_of_hours_bods = total_build_hours_bods + total_build_hours_bods_recon
        number_of_hours_dl = number_of_days_dl*9*etlr_number_of_objects
        number_of_hours_dq = dq_number_of_objects*number_of_days_dq*9

        return number_of_hours_bods, number_of_hours_dl, number_of_hours_dq


    vlow_objects_bods_hours, vlow_objects_dl_hours, vlow_objects_dq_hours = calculate_hours_per_complexity(etlr_number_of_vlow_objects, 1, 0.15, 0.5, dv_total_objects, 1.35, dq_number_of_vlow_objects, 1)

    low_objects_bods_hours, low_objects_dl_hours, low_objects_dq_hours = calculate_hours_per_complexity(etlr_number_of_low_objects, 4, 0.2, 1, dv_total_objects, 7.2, dq_number_of_low_objects, 3)

    medium_objects_bods_hours, medium_objects_dl_hours, medium_objects_dq_hours = calculate_hours_per_complexity(etlr_number_of_medium_objects, 8, 2, 1.5, dv_total_objects, 7.2, dq_number_of_medium_objects, 6.5)

    high_objects_bods_hours, high_objects_dl_hours, high_objects_dq_hours = calculate_hours_per_complexity(etlr_number_of_high_objects, 11, 4, 2, dv_total_objects, 11.88, dq_number_of_high_objects, 9)

    vhigh_objects_bods_hours, vhigh_objects_dl_hours, vhigh_objects_dq_hours = calculate_hours_per_complexity(etlr_number_of_vhigh_objects, 15, 5, 3, dv_total_objects, 16.2, dq_number_of_vhigh_objects, 12)


    dl_total_objects = etlr_total_objects
    total_bods_hours = vlow_objects_bods_hours + low_objects_bods_hours + medium_objects_bods_hours + high_objects_bods_hours + vhigh_objects_bods_hours
    total_dl_hours = vlow_objects_dl_hours + low_objects_dl_hours + medium_objects_dl_hours + high_objects_dl_hours + vhigh_objects_dl_hours
    total_dq_hours = vlow_objects_dq_hours + low_objects_dq_hours + medium_objects_dq_hours + high_objects_dq_hours + vhigh_objects_dq_hours


    def calculate_hours_per_phase (number_of_hours_dl, number_of_hours_bods, number_of_hours_dq):

        total_build_hours = number_of_hours_bods + number_of_hours_dl
        design_build = number_of_hours_bods + number_of_hours_dq
        mock1 = number_of_hours_dl*3/10
        mock2 = number_of_hours_dl*85/100
        mock3 = number_of_hours_dl
        prod = number_of_hours_dl
        workflow_enhancement_hours = design_build + (mock1*1/10)
        iptesting = workflow_enhancement_hours*5/100
        go_live_dep = workflow_enhancement_hours*4/100
        sub_tot = mock1 + mock2 + mock3 + prod + workflow_enhancement_hours + iptesting + go_live_dep 
        off_shore_data_lead = sub_tot*12/100
        grand_tot_hours = sub_tot + off_shore_data_lead

        return design_build, mock1, mock2, mock3, prod, workflow_enhancement_hours, iptesting, go_live_dep, sub_tot, off_shore_data_lead, grand_tot_hours 


    design_build, p1_mock1, p1_mock2, p1_mock3, p1_prod, p1_workflow_enhancement_hours, p1_iptesting, p1_go_live_dep, p1_sub_tot, p1_off_shore_data_lead, total_hours_phase_1  = calculate_hours_per_phase(total_dl_hours, total_bods_hours, total_dq_hours)
    total_dl_hours_phase_1 = total_hours_phase_1 - total_bods_hours - total_dq_hours
    total_dl_hours_phase_2 = 0
    total_dl_hours_phase_3 = 0
    grand_total_hours = total_dl_hours_phase_1 + total_dl_hours_phase_2 + total_dl_hours_phase_3

    def calculate_resource (project_timeline, total_hours):
        resource_count = math.ceil(total_hours / (180*project_timeline))

        if resource_count == 1:
            number_of_SC = 1
            number_of_C = 0
        elif resource_count == 2:
            number_of_SC = 1
            number_of_C = 1 
        elif resource_count == 3:
            number_of_SC = 1
            number_of_C = 2        
        elif resource_count == 4:
            number_of_SC = 1
            number_of_C = 3
        elif resource_count == 5:
            number_of_SC = 2
            number_of_C = 3
        elif resource_count == 6:
            number_of_SC = 2
            number_of_C = 4
        elif resource_count == 7:
            number_of_SC = 2
            number_of_C = 5
        elif resource_count == 8:
            number_of_SC = 3
            number_of_C = 5
        elif resource_count == 9:
            number_of_SC = 3
            number_of_C = 6     
        elif resource_count == 10:
            number_of_SC = 4
            number_of_C = 6 
        else:
            print('Number of resources required for the job exceeds 10')

        return resource_count, number_of_SC, number_of_C

    project_timeline = int(request.form.get('project_timeline'))
    resource_count, number_of_SC, number_of_C = calculate_resource (project_timeline, grand_total_hours)

    return render_template('result.html', selected_objects=selected_objects,
    result1=etlr_total_objects, result2=round(total_bods_hours), result3=round(total_dl_hours), result4=round(total_hours_phase_1), result5=round(total_dl_hours_phase_1), 
    result6=round(p1_mock1), result7=round(p1_mock2), result8=round(p1_mock3), result9=round(p1_prod), result10=round(p1_workflow_enhancement_hours), result11=round(p1_iptesting), result12=round(p1_go_live_dep), result13=round(p1_sub_tot), result14=round(p1_off_shore_data_lead), result15=round(total_hours_phase_1),
    result16=etlr_number_of_vlow_objects, result17=etlr_number_of_low_objects, result18=etlr_number_of_medium_objects, result19=etlr_number_of_high_objects, result20=etlr_number_of_vhigh_objects, result21=etlr_total_objects,
    result22=round(vlow_objects_bods_hours), result23=round(low_objects_bods_hours), result24=round(medium_objects_bods_hours), result25=round(high_objects_bods_hours), result26=round(vhigh_objects_bods_hours), result27=round(total_bods_hours),
    result28=etlr_number_of_vlow_objects, result29=etlr_number_of_low_objects, result30=etlr_number_of_medium_objects, result31=etlr_number_of_high_objects, result32=etlr_number_of_vhigh_objects, result33=dl_total_objects,
    result34=round(vlow_objects_dl_hours), result35=round(low_objects_dl_hours), result36=round(medium_objects_dl_hours), result37=round(high_objects_dl_hours), result38=round(vhigh_objects_dl_hours), result39=round(total_dl_hours),
    result40=resource_count, result41=number_of_SC, result42=number_of_C,
    result43=dq_number_of_vlow_objects, result44=dq_number_of_low_objects, result45=dq_number_of_medium_objects, result46=dq_number_of_high_objects, result47=dq_number_of_vhigh_objects, result48=dq_total_objects,
    result49=round(vlow_objects_dq_hours), result50=round(low_objects_dq_hours), result51=round(medium_objects_dq_hours), result52=round(high_objects_dq_hours), result53=round(vhigh_objects_dq_hours), result54=round(total_dq_hours),
    result55=round(design_build))

if __name__ == "__main__":
    app.run(debug=True)