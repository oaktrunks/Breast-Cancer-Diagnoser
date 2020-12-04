import xml.etree.ElementTree as ET
from patient_data_model import PatientData


class XmlProcessor():
    # Parses XML string and returns PatientData object
    def parse_patient_data(self, data):
        root = ET.fromstring(data)

        data_dict = {
            PatientData.PATIENT: root[0].attrib['id']}
        for child in root[0]:
            data_dict[child.tag] = child.text
        patient_data = PatientData(data_dict)

        return patient_data

    # turns PatientData object into XML string
    def patient_data_to_xml(self, patient_data):
        dataset = ET.Element('Dataset')

        data_dict = patient_data.serialize()

        patient = ET.SubElement(dataset, PatientData.PATIENT)
        patient.set(
            'id', data_dict[PatientData.PATIENT])

        for tag in PatientData.XML_ORDER:
            ET.SubElement(patient, tag).text = data_dict[tag]

        xml_patient_data = ET.tostring(dataset)

        return xml_patient_data
