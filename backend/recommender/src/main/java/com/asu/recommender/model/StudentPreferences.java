package com.asu.recommender.model;

import java.util.ArrayList;
import java.util.List;

public class StudentPreferences {
	private List<StudentPreference> students;
	
	public StudentPreferences() {
		students = new ArrayList<StudentPreference>();
	}

	public List<StudentPreference> getStudents() {
		return students;
	}

	public void setStudents(List<StudentPreference> students) {
		this.students = students;
	}

}
