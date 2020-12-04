class PatientData():
    # XML Tags
    PATIENT = 'Patient'
    CLUMP_THICKESS = 'clump_thickness'
    UNIFORMITY_CELL_SIZE = 'uniformity_cell_size'
    UNIFORMITY_CELL_SHAPE = 'uniformity_cell_shape'
    MARGINAL_ADHESION = 'marginal_adhesion'
    SINGLE_EPITHELIAL_CELL_SIZE = 'single_epithelial_cell_size'
    BARE_NUCLEI = 'bare_nuclei'
    BLAND_CHROMATIN = 'bland_chromatin'
    NORMAL_NUCLEOLI = 'normal_nucleoli'
    MITOSES = 'mitoses'
    CLASS = 'class'

    XML_ORDER = [
        CLUMP_THICKESS,
        UNIFORMITY_CELL_SIZE,
        UNIFORMITY_CELL_SHAPE,
        MARGINAL_ADHESION,
        SINGLE_EPITHELIAL_CELL_SIZE,
        BARE_NUCLEI,
        BLAND_CHROMATIN,
        NORMAL_NUCLEOLI,
        MITOSES,
        CLASS
    ]

    def __init__(self, patient_data):
        self.patient = patient_data[self.PATIENT]
        self.clump_thickness = patient_data[self.CLUMP_THICKESS]
        self.uniformity_cell_size = patient_data[self.UNIFORMITY_CELL_SIZE]
        self.uniformity_cell_shape = patient_data[self.UNIFORMITY_CELL_SHAPE]
        self.marginal_adhesion = patient_data[self.MARGINAL_ADHESION]
        self.single_epithelial_cell_size = patient_data[self.SINGLE_EPITHELIAL_CELL_SIZE]
        self.bare_nuclei = patient_data[self.BARE_NUCLEI]
        self.bland_chromatin = patient_data[self.BLAND_CHROMATIN]
        self.normal_nucleoli = patient_data[self.NORMAL_NUCLEOLI]
        self.mitoses = patient_data[self.MITOSES]
        self.classification = patient_data[self.CLASS]

    def serialize(self):
        return {
            self.PATIENT: self.patient,
            self.CLUMP_THICKESS: self.clump_thickness,
            self.UNIFORMITY_CELL_SIZE: self.uniformity_cell_size,
            self.UNIFORMITY_CELL_SHAPE: self.uniformity_cell_shape,
            self.MARGINAL_ADHESION: self.marginal_adhesion,
            self.SINGLE_EPITHELIAL_CELL_SIZE: self.single_epithelial_cell_size,
            self.BARE_NUCLEI: self.bare_nuclei,
            self.BLAND_CHROMATIN: self.bland_chromatin,
            self.NORMAL_NUCLEOLI: self.normal_nucleoli,
            self.MITOSES: self.mitoses,
            self.CLASS: self.classification,
        }

    def toString(self):
        return (
            f"patient = {self.patient}\n"
            f"clump_thickness = {self.clump_thickness}\n"
            f"uniformity_cell_size = {self.uniformity_cell_size}\n"
            f"uniformity_cell_shape = {self.uniformity_cell_shape}\n"
            f"marginal_adhesion = {self.marginal_adhesion}\n"
            f"single_epithelial_cell_size = {self.single_epithelial_cell_size}\n"
            f"bare_nuclei = {self.bare_nuclei}\n"
            f"bland_chromatin = {self.bland_chromatin}\n"
            f"normal_nucleoli = {self.normal_nucleoli}\n"
            f"mitoses = {self.mitoses}\n"
            f"class = {self.classification}"
        )
