import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import axios from "axios";

function SharedProfilePage() {
    const { token } = useParams();
    const [profile, setProfile] = useState(null);

    useEffect(() => {
        axios.get(`http://127.0.0.1:8000/api/profile/share/${token}/`)
            .then(res => setProfile(res.data))
            .catch(() => setProfile("expired"));
    }, [token]);

    if (profile === "expired") return <h2>Link Expired</h2>;
    if (!profile) return <h2>Loading...</h2>;

    return (
        <div>
            <h2>{profile.full_name || "Unnamed User"}</h2>
            {profile.profile_photo && (
                <img src={`http://127.0.0.1:8000${profile.profile_photo}`} alt="Profile" />
            )}

            {/* Education */}
            <h3>Education</h3>
            {profile.educations?.map((edu, idx) => (
                <div key={idx}>
                    {edu.degree} - {edu.university} ({edu.year_of_completion}) | CGPA: {edu.marks_cgpa}
                </div>
            ))}

            {/* Work Experience */}
            <h3>Work Experience</h3>
            {profile.experiences?.map((exp, idx) => (
                <div key={idx}>
                    {exp.designation} at {exp.company_name} ({exp.start_date} - {exp.end_date})
                </div>
            ))}

            {/* Skills */}
            <h4>Skills: {profile.skills}</h4>

            {/* Resume */}
            {profile.resume && (
                <a href={`http://127.0.0.1:8000${profile.resume}`} download>
                    Download Resume
                </a>
            )}
        </div>
    );
}

export default SharedProfilePage;
