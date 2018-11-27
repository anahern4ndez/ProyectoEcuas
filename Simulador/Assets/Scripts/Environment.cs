using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Environment : MonoBehaviour {
    public GameObject edif2;
    public GameObject edif3;
    public GameObject edif4;
    public bool moviendo = false;
    private Vector3 posGameObject;
    private float corrimiento;

    // Use this for initialization
    void Start () {
        posGameObject = this.gameObject.transform.position; 
        StartCoroutine("CorutinaUpdatePos");

    }
	
	// Update is called once per frame
	void Update () {
		
	}
    IEnumerator CorutinaUpdatePos()
    {
        while (moviendo)
        {
            yield return new WaitForSeconds(0.1f);
            //promedios de posiciones
            corrimiento = (edif2.gameObject.transform.position.x + edif3.gameObject.transform.position.x + edif4.gameObject.transform.position.x)/3.0f;
            this.gameObject.transform.position = new Vector3(this.gameObject.transform.position.x + corrimiento, this.gameObject.transform.position.y, this.gameObject.transform.position.z);
        }
    }
}
