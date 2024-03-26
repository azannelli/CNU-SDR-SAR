# CNU-SDR-SAR[
https://static.wikia.nocookie.net/cnu-jefferson-lab/images/e/eb/PCSE-2.jpg/revision/latest/scale-to-width-down/1000?cb=20140618180912
Christopher Newport University Senior Capstone Project for building a Synthetic Aperture Radar using a moving Software Defined Radio
This project aims to showcase and demonstrate the implementation of a Software Defined Radio (SDR) to create a functional Synthetic Aperture Radar (SAR). SAR is a type of radar used to generate two-dimensional images or three-dimensional reconstructions of objects, such as landscapes, by collecting reflected energy. The SAR will relay waveform data and render pictures. 
ASPIRE, the primary customer for SAR creation, has identified a significant issue—a pronounced phase shift present within the system and its collective data. The objective is to develop a functional SAR while minimizing this phase shift. Phase shift is the difference in position of a wave at a given point in time compared to the position of the same wave at the same point in time in another location [5]. To address this specific problem, the group plans to leverage data from the moving step motor and a GPS disciplined oscillator (GPSDO) to eliminate, or at least reduce, any phase shifts within the system. A GPSDO is a combination of a GPS receiver and a high-quality, stable oscillator such as a quartz or rubidium oscillator whose output is controlled to agree with the signals broadcast by GPS or other GNSS satellites [4]. During the use of the step motor, all collected data about its movement will be mathematically calculated to maintain a detailed log of the rig and its position while in motion. For precise and detailed positioning of the rig, the GPSDO will operate in parallel with a GPS antenna locked onto a GPS service. This configuration will enable the rig to transmit its position to the connected PC station effectively. With these two factors in play, the phase shift should theoretically be minimized to insignificance.
