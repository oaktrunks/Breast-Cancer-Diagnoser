import tkinter as tk
from patient_data_model import PatientData


class PatientDataEntryScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.create_widgets()

    def create_widgets(self):
        """
        Function does the initial page setup
        """

        # Patient data input fields
        tk.Label(self, text="Patient ID").grid(row=0)
        self.patient_id = tk.Entry(self)
        self.patient_id.grid(row=0, column=1)

        tk.Label(self, text="Clump Thickness").grid(row=1)
        self.clump_thickness = tk.Entry(self)
        self.clump_thickness.grid(row=1, column=1)

        tk.Label(self, text="Uniformity Cell Size").grid(row=2)
        self.uniformity_cell_size = tk.Entry(self)
        self.uniformity_cell_size.grid(row=2, column=1)

        tk.Label(self, text="Uniformity Cell Shape").grid(row=3)
        self.uniformity_cell_shape = tk.Entry(self)
        self.uniformity_cell_shape.grid(row=3, column=1)

        tk.Label(self, text="Marginal Adhesion").grid(row=4)
        self.marginal_adhesion = tk.Entry(self)
        self.marginal_adhesion.grid(row=4, column=1)

        tk.Label(self, text="Single Epithelial Cell Size").grid(row=5)
        self.single_epithelial_cell_size = tk.Entry(self)
        self.single_epithelial_cell_size.grid(row=5, column=1)

        tk.Label(self, text="Bare Nuclei").grid(row=6)
        self.bare_nuclei = tk.Entry(self)
        self.bare_nuclei.grid(row=6, column=1)

        tk.Label(self, text="Bland Chromatin").grid(row=7)
        self.bland_chromatin = tk.Entry(self)
        self.bland_chromatin.grid(row=7, column=1)

        tk.Label(self, text="Normal Nucleoli").grid(row=8)
        self.normal_nucleoli = tk.Entry(self)
        self.normal_nucleoli.grid(row=8, column=1)

        tk.Label(self, text="Mitoses").grid(row=9)
        self.mitoses = tk.Entry(self)
        self.mitoses.grid(row=9, column=1)
        # End of patient data input fields

        # Request Status
        self.request_text = tk.StringVar(self)
        self.request_text.set("Status: Request not yet sent")
        self.request_status = tk.Label(self, textvariable=self.request_text)
        self.request_status.grid(row=10, columnspan=2, pady=20)

        # Send Request button
        self.send_request_button = tk.Button(self)
        self.send_request_button["text"] = "Send diagnosis request"
        self.send_request_button["command"] = self.send_request
        self.send_request_button.grid(row=11, columnspan=2, pady=20)

        # Back button
        self.back_button = tk.Button(self, text="Back",
                                     command=self.back_action)
        self.back_button.grid(row=12, columnspan=2, pady=20)

    def send_request(self):
        majority_vote = self.controller.request_manager.send_request(PatientData({
            PatientData.PATIENT: self.patient_id.get(),
            PatientData.CLUMP_THICKESS: self.clump_thickness.get(),
            PatientData.UNIFORMITY_CELL_SIZE: self.uniformity_cell_size.get(),
            PatientData.UNIFORMITY_CELL_SHAPE: self.uniformity_cell_shape.get(),
            PatientData.MARGINAL_ADHESION: self.marginal_adhesion.get(),
            PatientData.SINGLE_EPITHELIAL_CELL_SIZE: self.single_epithelial_cell_size.get(),
            PatientData.BARE_NUCLEI: self.bare_nuclei.get(),
            PatientData.BLAND_CHROMATIN: self.bland_chromatin.get(),
            PatientData.NORMAL_NUCLEOLI: self.normal_nucleoli.get(),
            PatientData.MITOSES: self.mitoses.get(),
            PatientData.CLASS: None,
        }))
        result = 'has' if majority_vote is '4' else 'does not have'
        self.request_text.set("Result: Patient {} cancer".format(result))

    def back_action(self):
        self.controller.show_frame('HomeScreen')
