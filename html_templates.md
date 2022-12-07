```html
dashboard
<div class="container">
    <div class="row">
        <h1>Student Grades</h1>
        <div class="panel panel-default">
            <div class="panel-body">
                Demo of prefilled student grade table. To add grades, select a course and grade then press "Add Grade".
            </div>
        </div>
        <table class="table table-bordered student-grade-table">
            <thead>
                <tr>
                    <th>Student Name</th>
                    <th>Term</th>
                    <th>Course</th>
                    <th>Credits</th>
                    <th>Grade</th>
                    <th>Actions</th>
                </tr>
            </thead>
            <tbody>
                <tr class="student-saved-row">
                    <th>Matt Bain</th>
                    <td>Winter 2016</td>
                    <td>
                        <span class="course" data-course-code="C2">Course 2</span>
                        <select class="course-select form-control input-sm" name="course">
                            <option value="" data-credits="">- Select Course -</option>
                            <option data-credits="4" value="C1">Course 1</option>
                            <option data-credits="12" value="C2" selected>Course 2</option>
                            <option data-credits="8" value="C3">Course 3</option>
                            <option data-credits="2" value="C4">Course 4</option>
                            <option data-credits="3" value="C5">Course 5</option>
                        </select>
                    </td>
                    <td><span class="credits">12</span></td>
                    <td>
                        <span class="grade" data-grade-val="Pass">Pass</span>
                        <select name="" id="" class="grade-select form-control input-sm">
                            <option value="">- Select Grade -</option>
                            <optgroup label="Pass/Fail">
                                <option value="Pass" selected>Pass</option>
                                <option value="Fail">Fail</option>
                            </optgroup>
                            <optgroup label="Letter Grade">
                                <option value="A+">A+</option>
                                <option value="A">A</option>
                                <option value="A-">A-</option>
                                <option value="B+">B+</option>
                                <option value="B">B</option>
                                <option value="B-">B-</option>
                                <option value="C+">C+</option>
                                <option value="C">C</option>
                                <option value="D">D</option>
                                <option value="F">F</option>
                            </optgroup>
                            <optgroup label="Other">
                                <option value="Audit">Audit</option>
                                <option value="Withdrawl">Withdrawl</option>
                            </optgroup>
                        </select>
                    </td>
                    <td>
                        <button class="add btn btn-success btn-xs">Add Grade</button>
                        <button class="edit btn btn-warning btn-xs">Edit</button>
                        <button class="save btn btn-primary btn-xs">Save</button>
                        <button class="delete btn btn-danger btn-xs" title="Delete"><span class="glyphicon glyphicon-remove"></span></button>
                    </td>
                </tr>
                <tr class="student-saved-row">
                    <th>Matt Bain</th>
                    <td>Winter 2016</td>
                    <td>
                        <span class="course" data-course-code="C4">Course 4</span>
                        <select class="course-select form-control input-sm" name="course">
                            <option value="" data-credits="">- Select Course -</option>
                            <option data-credits="4" value="C1">Course 1</option>
                            <option data-credits="12" value="C2">Course 2</option>
                            <option data-credits="8" value="C3">Course 3</option>
                            <option data-credits="2" value="C4" selected>Course 4</option>
                            <option data-credits="3" value="C5">Course 5</option>
                        </select>
                    </td>
                    <td><span class="credits">2</span></td>
                    <td>
                        <span class="grade" data-grade-val="A-">A-</span>
                        <select name="" id="" class="grade-select form-control input-sm">
                            <option value="">- Select Grade -</option>
                            <optgroup label="Pass/Fail">
                                <option value="Pass">Pass</option>
                                <option value="Fail">Fail</option>
                            </optgroup>
                            <optgroup label="Letter Grade">
                                <option value="A+">A+</option>
                                <option value="A">A</option>
                                <option value="A-" selected>A-</option>
                                <option value="B+">B+</option>
                                <option value="B">B</option>
                                <option value="B-">B-</option>
                                <option value="C+">C+</option>
                                <option value="C">C</option>
                                <option value="D">D</option>
                                <option value="F">F</option>
                            </optgroup>
                            <optgroup label="Other">
                                <option value="Audit">Audit</option>
                                <option value="Withdrawl">Withdrawl</option>
                            </optgroup>
                        </select>
                    </td>
                    <td>
                        <button class="add btn btn-success btn-xs">Add Grade</button>
                        <button class="edit btn btn-warning btn-xs">Edit</button>
                        <button class="save btn btn-primary btn-xs">Save</button>
                        <button class="delete btn btn-danger btn-xs" title="Delete"><span class="glyphicon glyphicon-remove"></span></button>
                    </td>
                </tr>
                <tr class="student-new-row active">
                    <th>Matt Bain</th>
                    <td>Winter 2016</td>
                    <td>
                        <span class="course" data-course-code=""></span>
                        <select class="course-select form-control input-sm" name="course">
                            <option value="" data-credits="">- Select Course -</option>
                            <option data-credits="4" value="C1">Course 1</option>
                            <option data-credits="12" value="C2">Course 2</option>
                            <option data-credits="8" value="C3">Course 3</option>
                            <option data-credits="2" value="C4">Course 4</option>
                            <option data-credits="3" value="C5">Course 5</option>
                        </select>
                    </td>
                    <td><span class="credits"></span></td>
                    <td>
                        <span class="grade"></span>
                        <select name="" id="" class="grade-select form-control input-sm">
                            <option value="">- Select Grade -</option>
                            <optgroup label="Pass/Fail">
                                <option value="Pass">Pass</option>
                                <option value="Fail">Fail</option>
                            </optgroup>
                            <optgroup label="Letter Grade">
                                <option value="A+">A+</option>
                                <option value="A">A</option>
                                <option value="A-">A-</option>
                                <option value="B+">B+</option>
                                <option value="B">B</option>
                                <option value="B-">B-</option>
                                <option value="C+">C+</option>
                                <option value="C">C</option>
                                <option value="D">D</option>
                                <option value="F">F</option>
                            </optgroup>
                            <optgroup label="Other">
                                <option value="Audit">Audit</option>
                                <option value="Withdrawl">Withdrawl</option>
                            </optgroup>
                        </select>
                    </td>
                    <td>
                        <button class="add btn btn-success btn-xs">Add Grade</button>
                        <button class="edit btn btn-warning btn-xs">Edit</button>
                        <button class="save btn btn-primary btn-xs">Save</button>
                        <button class="delete btn btn-danger btn-xs" title="Delete"><span class="glyphicon glyphicon-remove"></span></button>
                    </td>
                </tr>
                <tr class="student-saved-row">
                    <th>Jono Manion</th>
                    <td>Winter 2016</td>
                    <td>
                        <span class="course" data-course-code="C3">Course 3</span>
                        <select class="course-select form-control input-sm" name="course">
                            <option value="">- Select Course -</option>
                            <option data-credits="4" value="C1">Course 1</option>
                            <option data-credits="12" value="C2">Course 2</option>
                            <option data-credits="8" value="C3" selected>Course 3</option>
                            <option data-credits="2" value="C4">Course 4</option>
                            <option data-credits="3" value="C5">Course 5</option>
                        </select>
                    </td>
                    <td><span class="credits">8</span></td>
                    <td>
                        <span class="grade" data-grade-val="B+">B+</span>
                        <select name="" id="" class="grade-select form-control input-sm">
                            <option value="">- Select Grade -</option>
                            <optgroup label="Pass/Fail">
                                <option value="Pass">Pass</option>
                                <option value="Fail">Fail</option>
                            </optgroup>
                            <optgroup label="Letter Grade">
                                <option value="A+">A+</option>
                                <option value="A">A</option>
                                <option value="A-">A-</option>
                                <option value="B+" selected>B+</option>
                                <option value="B">B</option>
                                <option value="B-">B-</option>
                                <option value="C+">C+</option>
                                <option value="C">C</option>
                                <option value="D">D</option>
                                <option value="F">F</option>
                            </optgroup>
                            <optgroup label="Other">
                                <option value="Audit">Audit</option>
                                <option value="Withdrawl">Withdrawl</option>
                            </optgroup>
                        </select>
                    </td>
                    <td>
                        <button class="add btn btn-success btn-xs">Add Grade</button>
                        <button class="edit btn btn-warning btn-xs">Edit</button>
                        <button class="save btn btn-primary btn-xs">Save</button>
                        <button class="delete btn btn-danger btn-xs" title="Delete"><span class="glyphicon glyphicon-remove"></span></button>
                    </td>
                </tr>
                <tr class="student-saved-row">
                    <th>Jono Manion</th>
                    <td>Winter 2016</td>
                    <td>
                        <span class="course" data-course-code="C1">Course 1</span>
                        <select class="course-select form-control input-sm" name="course">
                            <option value="">- Select Course -</option>
                            <option data-credits="4" value="C1" selected>Course 1</option>
                            <option data-credits="12" value="C2">Course 2</option>
                            <option data-credits="8" value="C3">Course 3</option>
                            <option data-credits="2" value="C4">Course 4</option>
                            <option data-credits="3" value="C5">Course 5</option>
                        </select>
                    </td>
                    <td><span class="credits">4</span></td>
                    <td>
                        <span class="grade" data-grade-val="A+">A+</span>
                        <select name="" id="" class="grade-select form-control input-sm">
                            <option value="">- Select Grade -</option>
                            <optgroup label="Pass/Fail">
                                <option value="Pass">Pass</option>
                                <option value="Fail">Fail</option>
                            </optgroup>
                            <optgroup label="Letter Grade">
                                <option value="A+" selected>A+</option>
                                <option value="A">A</option>
                                <option value="A-">A-</option>
                                <option value="B+">B+</option>
                                <option value="B">B</option>
                                <option value="B-">B-</option>
                                <option value="C+">C+</option>
                                <option value="C">C</option>
                                <option value="D">D</option>
                                <option value="F">F</option>
                            </optgroup>
                            <optgroup label="Other">
                                <option value="Audit">Audit</option>
                                <option value="Withdrawl">Withdrawl</option>
                            </optgroup>
                        </select>
                    </td>
                    <td>
                        <button class="add btn btn-success btn-xs">Add Grade</button>
                        <button class="edit btn btn-warning btn-xs">Edit</button>
                        <button class="save btn btn-primary btn-xs">Save</button>
                        <button class="delete btn btn-danger btn-xs" title="Delete"><span class="glyphicon glyphicon-remove"></span></button>
                    </td>
                </tr>
                <tr class="student-new-row active">
                    <th>Jono Manion</th>
                    <td>Winter 2016</td>
                    <td>
                        <span class="course" data-course-code=""></span>
                        <select class="course-select form-control input-sm" name="course">
                            <option value="">- Select Course -</option>
                            <option data-credits="4" value="C1">Course 1</option>
                            <option data-credits="12" value="C2">Course 2</option>
                            <option data-credits="8" value="C3">Course 3</option>
                            <option data-credits="2" value="C4">Course 4</option>
                            <option data-credits="3" value="C5">Course 5</option>
                        </select>
                    </td>
                    <td><span class="credits"></span></td>
                    <td>
                        <span class="grade"></span>
                        <select name="" id="" class="grade-select form-control input-sm">
                            <option value="">- Select Grade -</option>
                            <optgroup label="Pass/Fail">
                                <option value="Pass">Pass</option>
                                <option value="Fail">Fail</option>
                            </optgroup>
                            <optgroup label="Letter Grade">
                                <option value="A+">A+</option>
                                <option value="A">A</option>
                                <option value="A-">A-</option>
                                <option value="B+">B+</option>
                                <option value="B">B</option>
                                <option value="B-">B-</option>
                                <option value="C+">C+</option>
                                <option value="C">C</option>
                                <option value="D">D</option>
                                <option value="F">F</option>
                            </optgroup>
                            <optgroup label="Other">
                                <option value="Audit">Audit</option>
                                <option value="Withdrawl">Withdrawl</option>
                            </optgroup>
                        </select>
                    </td>
                    <td>
                        <button class="add btn btn-success btn-xs">Add Grade</button>
                        <button class="edit btn btn-warning btn-xs">Edit</button>
                        <button class="save btn btn-primary btn-xs">Save</button>
                        <button class="delete btn btn-danger btn-xs" title="Delete"><span class="glyphicon glyphicon-remove"></span></button>
                    </td>
                </tr>
                <tr class="student-saved-row">
                    <th>Kayla Thompson</th>
                    <td>Winter 2016</td>
                    <td>
                        <span class="course" data-course-code="C4">Course 4</span>
                        <select class="course-select form-control input-sm" name="course">
                            <option value="">- Select Course -</option>
                            <option data-credits="4" value="C1">Course 1</option>
                            <option data-credits="12" value="C2">Course 2</option>
                            <option data-credits="8" value="C3">Course 3</option>
                            <option data-credits="2" value="C4" selected>Course 4</option>
                            <option data-credits="3" value="C5">Course 5</option>
                        </select>
                    </td>
                    <td><span class="credits">2</span></td>
                    <td>
                        <span class="grade" data-grade-val="A">A</span>
                        <select name="" id="" class="grade-select form-control input-sm">
                            <option value="">- Select Grade -</option>
                            <optgroup label="Pass/Fail">
                                <option value="Pass">Pass</option>
                                <option value="Fail">Fail</option>
                            </optgroup>
                            <optgroup label="Letter Grade">
                                <option value="A+">A+</option>
                                <option value="A" selected>A</option>
                                <option value="A-">A-</option>
                                <option value="B+">B+</option>
                                <option value="B">B</option>
                                <option value="B-">B-</option>
                                <option value="C+">C+</option>
                                <option value="C">C</option>
                                <option value="D">D</option>
                                <option value="F">F</option>
                            </optgroup>
                            <optgroup label="Other">
                                <option value="Audit">Audit</option>
                                <option value="Withdrawl">Withdrawl</option>
                            </optgroup>
                        </select>
                    </td>
                    <td>
                        <button class="add btn btn-success btn-xs">Add Grade</button>
                        <button class="edit btn btn-warning btn-xs">Edit</button>
                        <button class="save btn btn-primary btn-xs">Save</button>
                        <button class="delete btn btn-danger btn-xs" title="Delete"><span class="glyphicon glyphicon-remove"></span></button>
                    </td>
                </tr>
                <tr class="student-saved-row">
                    <th>Kayla Thompson</th>
                    <td>Winter 2016</td>
                    <td>
                        <span class="course" data-course-code="C5">Course 5</span>
                        <select class="course-select form-control input-sm" name="course">
                            <option value="">- Select Course -</option>
                            <option data-credits="4" value="C1">Course 1</option>
                            <option data-credits="12" value="C2">Course 2</option>
                            <option data-credits="8" value="C3">Course 3</option>
                            <option data-credits="2" value="C4">Course 4</option>
                            <option data-credits="3" value="C5" selected>Course 5</option>
                        </select>
                    </td>
                    <td><span class="credits">3</span></td>
                    <td>
                        <span class="grade" data-grade-val="A+">A+</span>
                        <select name="" id="" class="grade-select form-control input-sm">
                            <option value="">- Select Grade -</option>
                            <optgroup label="Pass/Fail">
                                <option value="Pass">Pass</option>
                                <option value="Fail">Fail</option>
                            </optgroup>
                            <optgroup label="Letter Grade">
                                <option value="A+" selected>A+</option>
                                <option value="A">A</option>
                                <option value="A-">A-</option>
                                <option value="B+">B+</option>
                                <option value="B">B</option>
                                <option value="B-">B-</option>
                                <option value="C+">C+</option>
                                <option value="C">C</option>
                                <option value="D">D</option>
                                <option value="F">F</option>
                            </optgroup>
                            <optgroup label="Other">
                                <option value="Audit">Audit</option>
                                <option value="Withdrawl">Withdrawl</option>
                            </optgroup>
                        </select>
                    </td>
                    <td>
                        <button class="add btn btn-success btn-xs">Add Grade</button>
                        <button class="edit btn btn-warning btn-xs">Edit</button>
                        <button class="save btn btn-primary btn-xs">Save</button>
                        <button class="delete btn btn-danger btn-xs" title="Delete"><span class="glyphicon glyphicon-remove"></span></button>
                    </td>
                </tr>
                <tr class="student-new-row active">
                    <th>Kayla Thompson</th>
                    <td>Winter 2016</td>
                    <td>
                        <span class="course" data-course-code=""></span>
                        <select class="course-select form-control input-sm" name="course">
                            <option value="">- Select Course -</option>
                            <option data-credits="4" value="C1">Course 1</option>
                            <option data-credits="12" value="C2">Course 2</option>
                            <option data-credits="8" value="C3">Course 3</option>
                            <option data-credits="2" value="C4">Course 4</option>
                            <option data-credits="3" value="C5">Course 5</option>
                        </select>
                    </td>
                    <td><span class="credits"></span></td>
                    <td>
                        <span class="grade"></span>
                        <select name="" id="" class="grade-select form-control input-sm">
                            <option value="">- Select Grade -</option>
                            <optgroup label="Pass/Fail">
                                <option value="Pass">Pass</option>
                                <option value="Fail">Fail</option>
                            </optgroup>
                            <optgroup label="Letter Grade">
                                <option value="A+">A+</option>
                                <option value="A">A</option>
                                <option value="A-">A-</option>
                                <option value="B+">B+</option>
                                <option value="B">B</option>
                                <option value="B-">B-</option>
                                <option value="C+">C+</option>
                                <option value="C">C</option>
                                <option value="D">D</option>
                                <option value="F">F</option>
                            </optgroup>
                            <optgroup label="Other">
                                <option value="Audit">Audit</option>
                                <option value="Withdrawl">Withdrawl</option>
                            </optgroup>
                        </select>
                    </td>
                    <td>
                        <button class="add btn btn-success btn-xs">Add Grade</button>
                        <button class="edit btn btn-warning btn-xs">Edit</button>
                        <button class="save btn btn-primary btn-xs">Save</button>
                        <button class="delete btn btn-danger btn-xs" title="Delete"><span class="glyphicon glyphicon-remove"></span></button>
                    </td>
                </tr>
                <tr class="student-saved-row">
                    <th>Curtis Lawrence</th>
                    <td>Winter 2016</td>
                    <td>
                        <span class="course" data-course-code="C1">Course 1</span>
                        <select class="course-select form-control input-sm" name="course">
                            <option value="">- Select Course -</option>
                            <option data-credits="4" value="C1" selected>Course 1</option>
                            <option data-credits="12" value="C2">Course 2</option>
                            <option data-credits="8" value="C3">Course 3</option>
                            <option data-credits="2" value="C4">Course 4</option>
                            <option data-credits="3" value="C5">Course 5</option>
                        </select>
                    </td>
                    <td><span class="credits">4</span></td>
                    <td>
                        <span class="grade" data-grade-val="D">D</span>
                        <select name="" id="" class="grade-select form-control input-sm">
                            <option value="">- Select Grade -</option>
                            <optgroup label="Pass/Fail">
                                <option value="Pass">Pass</option>
                                <option value="Fail">Fail</option>
                            </optgroup>
                            <optgroup label="Letter Grade">
                                <option value="A+">A+</option>
                                <option value="A">A</option>
                                <option value="A-">A-</option>
                                <option value="B+">B+</option>
                                <option value="B">B</option>
                                <option value="B-">B-</option>
                                <option value="C+">C+</option>
                                <option value="C">C</option>
                                <option value="D" selected>D</option>
                                <option value="F">F</option>
                            </optgroup>
                            <optgroup label="Other">
                                <option value="Audit">Audit</option>
                                <option value="Withdrawl">Withdrawl</option>
                            </optgroup>
                        </select>
                    </td>
                    <td>
                        <button class="add btn btn-success btn-xs">Add Grade</button>
                        <button class="edit btn btn-warning btn-xs">Edit</button>
                        <button class="save btn btn-primary btn-xs">Save</button>
                        <button class="delete btn btn-danger btn-xs" title="Delete"><span class="glyphicon glyphicon-remove"></span></button>
                    </td>
                </tr>
                <tr class="student-new-row active">
                    <th>Curtis Lawrence</th>
                    <td>Winter 2016</td>
                    <td>
                        <span class="course" data-course-code=""></span>
                        <select class="course-select form-control input-sm" name="course">
                            <option value="">- Select Course -</option>
                            <option data-credits="4" value="C1">Course 1</option>
                            <option data-credits="12" value="C2">Course 2</option>
                            <option data-credits="8" value="C3">Course 3</option>
                            <option data-credits="2" value="C4">Course 4</option>
                            <option data-credits="3" value="C5">Course 5</option>
                        </select>
                    </td>
                    <td><span class="credits"></span></td>
                    <td>
                        <span class="grade"></span>
                        <select name="" id="" class="grade-select form-control input-sm">
                            <option value="">- Select Grade -</option>
                            <optgroup label="Pass/Fail">
                                <option value="Pass">Pass</option>
                                <option value="Fail">Fail</option>
                            </optgroup>
                            <optgroup label="Letter Grade">
                                <option value="A+">A+</option>
                                <option value="A">A</option>
                                <option value="A-">A-</option>
                                <option value="B+">B+</option>
                                <option value="B">B</option>
                                <option value="B-">B-</option>
                                <option value="C+">C+</option>
                                <option value="C">C</option>
                                <option value="D">D</option>
                                <option value="F">F</option>
                            </optgroup>
                            <optgroup label="Other">
                                <option value="Audit">Audit</option>
                                <option value="Withdrawl">Withdrawl</option>
                            </optgroup>
                        </select>
                    </td>
                    <td>
                        <button class="add btn btn-success btn-xs">Add Grade</button>
                        <button class="edit btn btn-warning btn-xs">Edit</button>
                        <button class="save btn btn-primary btn-xs">Save</button>
                        <button class="delete btn btn-danger btn-xs" title="Delete"><span class="glyphicon glyphicon-remove"></span></button>
                    </td>
                </tr>
                <tr class="student-new-row active">
                    <th>Stu Dent</th>
                    <td>Winter 2016</td>
                    <td>
                        <span class="course" data-course-code=""></span>
                        <select class="course-select form-control input-sm" name="course">
                            <option value="">- Select Course -</option>
                            <option data-credits="4" value="C1">Course 1</option>
                            <option data-credits="12" value="C2">Course 2</option>
                            <option data-credits="8" value="C3">Course 3</option>
                            <option data-credits="2" value="C4">Course 4</option>
                            <option data-credits="3" value="C5">Course 5</option>
                        </select>
                    </td>
                    <td><span class="credits"></span></td>
                    <td>
                        <span class="grade"></span>
                        <select name="" id="" class="grade-select form-control input-sm">
                            <option value="">- Select Grade -</option>
                            <optgroup label="Pass/Fail">
                                <option value="Pass">Pass</option>
                                <option value="Fail">Fail</option>
                            </optgroup>
                            <optgroup label="Letter Grade">
                                <option value="A+">A+</option>
                                <option value="A">A</option>
                                <option value="A-">A-</option>
                                <option value="B+">B+</option>
                                <option value="B">B</option>
                                <option value="B-">B-</option>
                                <option value="C+">C+</option>
                                <option value="C">C</option>
                                <option value="D">D</option>
                                <option value="F">F</option>
                            </optgroup>
                            <optgroup label="Other">
                                <option value="Audit">Audit</option>
                                <option value="Withdrawl">Withdrawl</option>
                            </optgroup>
                        </select>
                    </td>
                    <td>
                        <button class="add btn btn-success btn-xs">Add Grade</button>
                        <button class="edit btn btn-warning btn-xs">Edit</button>
                        <button class="save btn btn-primary btn-xs">Save</button>
                        <button class="delete btn btn-danger btn-xs" title="Delete"><span class="glyphicon glyphicon-remove"></span></button>
                    </td>
                </tr>
                <tr class="student-new-row active">
                    <th>Paula Pule </th>
                    <td>Winter 2016</td>
                    <td>
                        <span class="course" data-course-code=""></span>
                        <select class="course-select form-control input-sm" name="course">
                            <option value="">- Select Course -</option>
                            <option data-credits="4" value="C1">Course 1</option>
                            <option data-credits="12" value="C2">Course 2</option>
                            <option data-credits="8" value="C3">Course 3</option>
                            <option data-credits="2" value="C4">Course 4</option>
                            <option data-credits="3" value="C5">Course 5</option>
                        </select>
                    </td>
                    <td><span class="credits"></span></td>
                    <td>
                        <span class="grade"></span>
                        <select name="" id="" class="grade-select form-control input-sm">
                            <option value="">- Select Grade -</option>
                            <optgroup label="Pass/Fail">
                                <option value="Pass">Pass</option>
                                <option value="Fail">Fail</option>
                            </optgroup>
                            <optgroup label="Letter Grade">
                                <option value="A+">A+</option>
                                <option value="A">A</option>
                                <option value="A-">A-</option>
                                <option value="B+">B+</option>
                                <option value="B">B</option>
                                <option value="B-">B-</option>
                                <option value="C+">C+</option>
                                <option value="C">C</option>
                                <option value="D">D</option>
                                <option value="F">F</option>
                            </optgroup>
                            <optgroup label="Other">
                                <option value="Audit">Audit</option>
                                <option value="Withdrawl">Withdrawl</option>
                            </optgroup>
                        </select>
                    </td>
                    <td>
                        <button class="add btn btn-success btn-xs">Add Grade</button>
                        <button class="edit btn btn-warning btn-xs">Edit</button>
                        <button class="save btn btn-primary btn-xs">Save</button>
                        <button class="delete btn btn-danger btn-xs" title="Delete"><span class="glyphicon glyphicon-remove"></span></button>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
</div>
```

```css
.saved {
    animation: saved 1.5s linear;
}
.delete {
    float: right;
}
.student-saved-row {
    .edit, .delete, .course, .grade {
        display: inline-block;
    }
    .add, .save, .course-select, .grade-select {
        display: none;
    }
}
.student-new-row {
    .save, .edit, .delete {
        display: none;
    }
    .add {
        display: inline-block;
    }
}
.student-new-row{
    td, th {
        border-bottom: 2px solid #999 !important;
        font-weight: normal;
        font-style: italic;
    }
}
.editing {
    .save, .delete {
        display: inline-block;
    }
    .course-select, .grade-select {
        display: block;
    }
    .add, .edit, .course, .grade {
        display: none;
    }
}

@keyframes saved {
    0% {
        background: #dff0d8;
    }
    50% {
        background: #dff0d8;
    }
    100% {
        background: #fff;
    }
}
```