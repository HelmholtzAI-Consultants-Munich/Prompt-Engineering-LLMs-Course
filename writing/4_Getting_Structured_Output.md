## Exercise: Structuring Text Data for Downstream Applications

Below are sample reviews for healthcare providers. With the help of an LLM, reformat these reviews into a structured format, such as Markdown, JSON, XML, or any other format suitable for a downstream application. Think about an application in your daily work, where the structured output can be helpful. E.g., integration with analytics tools, databases, creating user-friendly visualizations on websites, etc.


### Hints
- The template pattern can help you define the structure of the output
- The tail generation pattern can also be helpful

### Text

```
Brighton Family Clinic:
Reviewer 1: "The staff at Brighton Family Clinic were warm and welcoming. Wait time was about 15 minutes, which is reasonable. The facility was clean, and I felt well taken care of. Overall, a great experience."
Reviewer 2: "Had to wait over 30 minutes past my appointment time at Brighton, but the care provided by Dr. Harrison was excellent. The clinic is well-maintained."
Reviewer 3: "Brighton Family Clinic offers exceptional care. The staff is friendly, and the clinic is always clean. My only gripe is the wait time, which can be unpredictable."

Metro City Hospital:
Reviewer 1: "Metro City Hospital's emergency department had a very long wait time, but the care was thorough and professional. The facility cleanliness could be improved."
Reviewer 2: "I visited Metro City Hospital for a minor surgery and was impressed by the professionalism of the staff and the cleanliness of the surgical area."
Reviewer 3: "My experience at Metro City Hospital was mixed. The staff were professional, but the wait times in the outpatient department were longer than I expected."

Lakeside Physical Therapy:
Reviewer 1: "The therapists at Lakeside are knowledgeable and caring. I've seen great improvement in my condition since starting therapy here. Highly recommend."
Reviewer 2: "Lakeside Physical Therapy has a clean, well-equipped facility. The staff are friendly, but scheduling can sometimes be difficult due to high demand."
Reviewer 3: "Excellent care at Lakeside Physical Therapy. The wait time for my first appointment was short, and the staff have been consistently supportive throughout my treatment."

Greenwood Mental Health Services:
Reviewer 1: "Greenwood Mental Health Services provided me with the support I needed during a tough time. The therapists are compassionate and skilled."
Reviewer 2: "While the wait time to get an appointment at Greenwood can be lengthy, the quality of care and the friendliness of the staff make it worth it."
Reviewer 3: "I have been going to Greenwood Mental Health Services for six months now. The facility is always clean, and the staff are very professional and understanding."
```