from django.db import models



class Category(models.Model):
    title = models.CharField(verbose_name="Category" , max_length=250)
    reg_date = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.title} ({self.reg_date})"

class Student(models.Model):
    name = models.CharField(verbose_name="Name", max_length=150)
    age = models.IntegerField(verbose_name="Age")
    number = models.IntegerField(verbose_name='Number')
    reg_date = models.DateField(auto_now_add=True)


    def __str__(self) -> str:
        return self.name  
    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"

class Interest(models.Model):
    title = models.CharField(verbose_name="Question category", max_length=150)
    students = models.ForeignKey(Student, verbose_name="Students", on_delete=models.CASCADE )
    quantity = models.IntegerField(verbose_name="Quantity:" ,  default=0)
    reg_date = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return f"[{self.students.name}] {self.students.number} {self.title}"

    class Meta:
        verbose_name = "Interest"
        verbose_name_plural = "Interests"

class Question(models.Model):
    question = models.CharField(verbose_name="Question", max_length=250)
    answers = models.ManyToManyField("Answer", verbose_name="Answers")
    category = models.ForeignKey(Category , verbose_name="Category" , on_delete=models.CASCADE)
    reg_date = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return f"[{self.id}] {self.question} ({self.reg_date})"  

    class Meta:
        ordering = ["?"]
        verbose_name = "Question"
        verbose_name_plural = "Questions"

class Answer(models.Model):
    answer = models.CharField(verbose_name="Answer", max_length=250)
    category = models.ForeignKey(Category , verbose_name="Category" , on_delete=models.CASCADE)
    reg_date = models.DateField(auto_now_add=True)


    def __str__(self) -> str:
        return f"[{self.id}] {self.answer}"  

    class Meta:
        verbose_name = "Answer"
        verbose_name_plural = "Answers" 
