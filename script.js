// Feature vectors (AI knowledge representation)
const drugFeatures = {
    "Ashwagandha": { sedation: 0.7, bleeding: 0.1, glucose: 0.2 },
    "Ginkgo":      { sedation: 0.1, bleeding: 0.8, glucose: 0.1 },
    "Turmeric":    { sedation: 0.0, bleeding: 0.4, glucose: 0.6 },

    "Diazepam":    { sedation: 0.9, bleeding: 0.0, glucose: 0.0 },
    "Aspirin":     { sedation: 0.0, bleeding: 0.9, glucose: 0.0 },
    "Metformin":   { sedation: 0.0, bleeding: 0.0, glucose: 0.8 }
};

// AI inference function
function predict() {

    const ayu = document.getElementById("ayurvedic").value;
    const modern = document.getElementById("modern").value;

    const a = drugFeatures[ayu];
    const m = drugFeatures[modern];

    // AI risk score calculation
    const sedationRisk = a.sedation * m.sedation;
    const bleedingRisk = a.bleeding * m.bleeding;
    const glucoseRisk  = a.glucose  * m.glucose;

    const totalRisk = sedationRisk + bleedingRisk + glucoseRisk;

    let riskLevel, explanation;

    if (totalRisk > 0.4) {
        riskLevel = "High";
        explanation = "Strong overlapping pharmacological effects detected";
    } else if (totalRisk > 0.15) {
        riskLevel = "Moderate";
        explanation = "Partial interaction risk based on AI scoring";
    } else {
        riskLevel = "Low";
        explanation = "Minimal interaction predicted by AI model";
    }

    document.getElementById("result").innerHTML =
        `<b>AI Risk Level:</b> ${riskLevel}<br>
         <b>Risk Score:</b> ${totalRisk.toFixed(2)}<br>
         <b>AI Explanation:</b> ${explanation}`;
}
