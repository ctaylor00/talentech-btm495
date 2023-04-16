import datetime

class Person:
    def __init__(self, email, password, name, phone_number, address):
        self.email = email
        self.password = password
        self.name = name
        self.phone_number = phone_number
        self.address = address

class Client(Person):
    def __init__(self, client_id, company_name, status, portal_link):
        # super().__init__(email, password, name, phone_number, address) # Commented out for simplicity for the demos, in a real scenario the Person class would be called to have the attributes from the abstract classes
        # List of Applications
        self.application = []
        # List of Jobs Posted
        self.job_post = []
        self.client_id = client_id
        self.company_name = company_name
        self.status = status
        self.portal_link = portal_link

class Candidate(Person):
    def __init__(self, candidate_id, resume, date_birth, interview_link, name):
        # super().__init__(email, password, name, phone_number, address) # Commented out for simplicity for the demos, in a real scenario the Person class would be called to have the attributes from the abstract classes
        # Added for demo 1 to simplify and not need to call the person class with all its additional attributes (I did comment it in the classes to understand)
        self.name = name
        # List of Applications
        self.application = []
        # List of Appointments
        self.appointment = []
        # List of Interviews
        self.interview = []
        self.candidate_id = candidate_id
        self.resume = resume
        self.date_birth = date_birth
        self.interview_link = interview_link

    # This method displays a list of available datetimes and prints them for the Candidate to view and select from
    def submit_availabilities(self):
        availabilities = []
        start_time = datetime.time(hour=9)
        end_time = datetime.time(hour=17)
        duration = datetime.timedelta(hours=1)
        current_time = datetime.datetime.combine(datetime.date.today(), start_time)
    
        while current_time.time() < end_time:
            availability_slot = current_time.strftime("%I:%M %p")
            availabilities.append(availability_slot)
            current_time += duration

        return availabilities
    
    # The Candidate then inputs his desired time slots, before submitting (in this case we use 0 to submit)
    def newAppointment(self, availabilities):
        print("Available Times:")
        for index, time in enumerate(availabilities):
            print(f"{index + 1}. {time}")
        
        selected_slots = []
        while True:
            selected_slot = input("Select a time slot number (0 to exit): ")
            if selected_slot == '0':
                break
            try:
                selected_slot = int(selected_slot)
                if selected_slot > 0 and selected_slot <= len(availabilities):
                    selected_time = availabilities[selected_slot - 1]
                    selected_slots.append(selected_time)
                    print(f"Selected time slot: {selected_time}")
                else:
                    print("Invalid slot number. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        
        return selected_slots

class Recruiter(Person):
    def __init__(self, recruiter_id, title_position, start_date):
        # super().__init__(email, password, name, phone_number, address) # Commented out for simplicity for the demos, in a real scenario the Person class would be called to have the attributes from the abstract classes
        # List with the Applications linked to the Recruiter
        self.application = []
        # List with the Appointments of the Recruiter
        self.appointment = []
        # List of Interviews
        self.interview = []
        # List of Interview Notes
        self.interview_notes = []
        # List of Job Posts
        self.job_post = []
        self.recruiter_id = recruiter_id
        self.title_position = title_position
        self.start_date = start_date

class JobPost:
    def __init__(self, job_id, name, job_expiration, job_description, job_title, job_posted_date, status):
        self.job_id = job_id
        self.name = name
        # It is a list of Applications for the Job Post
        self.application = []
        # Populates with a Client
        self.client = None
        self.job_expiration = job_expiration
        self.job_description = job_description
        self.job_title = job_title
        self.job_posted_date = job_posted_date
        # Populates with a Recruiter
        self.recruiter = None
        self.status = status

    @staticmethod
    def change_job_status(status):
        if status == "Submitted":
            return ["Job Post has been accepted", "Job Post has been rejected", "Job Post must be modified"]
        elif status == "Job Post has been accepted":
            return []
        elif status == "Job Post has been rejected":
            return []
        elif status == "Job Post must be modified":
            return ["Job Post has been accepted", "Job Post has been rejected"]
        else:
            raise ValueError("Invalid Job Status provided.")
        
    def update_status(self, new_status):
        self.status = new_status

class Appointment:
    def __init__(self, appointment_id, job_title, candidate):
        self.appointment_id = appointment_id
        self.job_title = job_title
        # Populates with a Recruiter
        self.recruiter = None
        # Populates with a Candidate
        self.candidate = candidate
        # Populates with an Interview
        self.interview = None
        # Populates with a date
        self.date = None
        # Populates with a time
        self.time = None
        # Populates with a list of availabilities
        self.availabilities = []

    def add_availability(self, date, time):
        self.availabilities.append((date, time))

    def select_availability(self, index):
        if 0 <= index < len(self.availabilities):
            self.date, self.time = self.availabilities[index]
            return True
        else:
            return False

    def __str__(self):
        return f"Appointment with {self.candidate.name} on {self.date} at {self.time} for {self.recruiter}."

class Application:
    def __init__(self, application_id, date, stage, resume):
        self.application_id = application_id
        # Populates with a Job Post
        self.job_post = None
        # Populates with a Candidate
        self.candidate = None
        # Populates with a Client
        self.client = None
        # Populates with a Recruiter
        self.recruiter = None
        self.date = date
        self.stage = stage
        self.resume = resume
        # Populates with Interview Notes
        self.interview_notes = None
    
    @staticmethod
    def change_application_stage(stage):
        if stage == "Submitted":
            return ["Recruiter has accepted Application", "Recruiter has rejected Application"]
        elif stage == "Recruiter has accepted Application":
            return ["Ready for review by Employer"]
        elif stage == "Recruiter has rejected Application":
            return []
        elif stage == "Ready for review by Employer":
            return ["Employer has accepted Application", "Employer has rejected Application"]
        elif stage == "Employer has accepted Application":
            return []
        elif stage == "Employer has rejected Application":
            return []
        else:
            raise ValueError("Invalid application stage provided.")
        
    def update_stage(self, new_stage):
        self.stage = new_stage

class Interview:
    def __init__(self, interview_id):
        self.interview_id = interview_id
        # Populates with a Recruiter
        self.recruiter = None
        # Populates with a Candidate
        self.candidate = None
        # Populates with an Appointment
        self.appointment = None

class InterviewNotes:
    def __init__(self, notes):
        # Populates with an Interview
        self.interview = None
        # Populates with a Recruiter
        self.recruiter = None
        self.notes = notes

def demo1():
    # Candidate submits availabilities
    candidate = Candidate("001", "resume.pdf", "01-01-1990", "zoom_link", "Jane Doe")
    availabilities = candidate.submit_availabilities()
    selected_slots = candidate.newAppointment(availabilities)
    print(f"The candidate has selected the following time slots: {selected_slots}")
    
    # Recruiter selects a time slot
    for index, time in enumerate(selected_slots):
        print(f"{index + 1}. {time}")
    selected_slot = int(input("Enter the time slot number you want to select: ")) - 1
    if 0 <= selected_slot < len(availabilities):
        appointment = Appointment("A001", "Software Engineer", candidate)
        appointment.add_availability(datetime.date.today(), availabilities[selected_slot])
        appointment.select_availability(0)
        appointment.recruiter = "John Doe"
        print(f"Appointment scheduled: {appointment}")
    else:
        print("Invalid time slot number. Please try again.")
    pass

def demo2():
# Define a list of stage options, in this case we are in the application acceptance/rejection stage
    stage_options = ["Recruiter has accepted Application", "Recruiter has rejected Application"]

# The Recruiter has to select a stage from the list of options
    print("Select a stage from the following options:")
    for i, stage in enumerate(stage_options):
        print(f"{i+1}. {stage}")
    selection = input("Enter the number of the stage you want to select: ")

    selection = int(selection)

    if selection < 1 or selection > len(stage_options):
        print("Invalid selection.")
    else:
        # Get the selected stage and create the Application object
        selected_stage = stage_options[selection-1]
        app = Application("1234", "2022-01-01", selected_stage, "resume.pdf")
        
        # Print the new stage of the Application object
        print(f"Stage: {app.stage}")
    pass

if __name__ == '__main__':
# Call Demo 1
    demo1()

# Call Demo 2
#    demo2()